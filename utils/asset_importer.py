# utils/asset_importer.py

from PIL import Image, ImageOps
import numpy as np
import os

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

class AssetImporter:
    def __init__(self, tile_size=32, bg_threshold=240):
        self.tile_size = tile_size
        self.bg_threshold = bg_threshold  # Helligkeitsschwelle für Hintergrund

    def load_image(self, path):
        img = Image.open(path).convert("RGBA")
        return img

    def auto_crop_alpha(self, img):
        """Zuschneiden anhand Alpha-Kanal (transparenz)"""
        arr = np.array(img)
        if arr.shape[2] == 4:
            alpha = arr[:, :, 3]
            ys, xs = np.where(alpha > 10)
            if ys.size and xs.size:
                bbox = (xs.min(), ys.min(), xs.max(), ys.max())
                return img.crop(bbox)
        return img

    def auto_crop_contour(self, img):
        """Zuschneiden anhand Kontur mit OpenCV (falls installiert)"""
        if not HAS_CV2:
            return img
        arr = np.array(img.convert("RGB"))
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, self.bg_threshold, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return img
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        return img.crop((x, y, x + w, y + h))

    def remove_background(self, img):
        """Hintergrund anhand Helligkeit entfernen (Hintergrund wird transparent)"""
        rgba = img.convert("RGBA")
        arr = np.array(rgba)
        r, g, b, a = arr.T
        mask = (r > self.bg_threshold) & (g > self.bg_threshold) & (b > self.bg_threshold)
        arr[..., 3][mask.T] = 0
        return Image.fromarray(arr)

    def fit_to_tile(self, img):
        """Bild proportional skalieren und zentrieren auf TILE_SIZE x TILE_SIZE"""
        img = ImageOps.contain(img, (self.tile_size, self.tile_size))
        canvas = Image.new("RGBA", (self.tile_size, self.tile_size), (0, 0, 0, 0))
        x = (self.tile_size - img.width) // 2
        y = (self.tile_size - img.height) // 2
        canvas.paste(img, (x, y))
        return canvas

    def generate_sprite_sheet(self, img, out_path):
        """Optional: Erstelle ein kleines Sprite-Sheet mit Original, gespiegelt, verkleinert"""
        frames = []
        frames.append(img)
        frames.append(ImageOps.mirror(img))
        # Optional: mehr Frames hier hinzufügen
        width = self.tile_size * len(frames)
        height = self.tile_size
        sheet = Image.new("RGBA", (width, height))
        for i, frame in enumerate(frames):
            sheet.paste(frame, (i * self.tile_size, 0))
        sheet.save(out_path)
        print(f"Sprite-Sheet gespeichert: {out_path}")

    def import_image(self, file_path, out_dir, make_sprites=False):
        """Gesamtablauf Import"""
        img = self.load_image(file_path)
        img = self.auto_crop_alpha(img)
        if HAS_CV2:
            img = self.auto_crop_contour(img)
        img = self.remove_background(img)
        img = self.fit_to_tile(img)

        os.makedirs(out_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        out_path = os.path.join(out_dir, f"{base_name}.png")
        img.save(out_path)
        print(f"Bild gespeichert: {out_path}")

        if make_sprites:
            sprite_path = os.path.join(out_dir, f"{base_name}_sheet.png")
            self.generate_sprite_sheet(img, sprite_path)