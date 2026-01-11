import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import sys
def find_and_click_template(template_path, threshold=0.8, scale_factor=2):
    """
    Find a template image on screen and click it.

    Args:
        template_path: Path to the template image (bounding box image)
        threshold: Matching confidence threshold (0-1)
        scale_factor: Retina display scale factor (usually 2 for Retina)
    """

    # Capture the screen
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Load the template image
    template = cv2.imread(template_path)
    if template is None:
        print(f"Error: Could not load template image from {template_path}")
        return False

    # Convert to grayscale for better matching
    screenshot_gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get template dimensions
    h, w = template_gray.shape

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(f"Best match confidence: {max_val:.3f}")

    if max_val >= threshold:
        # Get the center of the matched region
        top_left = max_loc
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2

        # Adjust for Retina display scaling
        click_x = center_x / scale_factor
        click_y = center_y / scale_factor

        print(f"Match found at: ({top_left[0]}, {top_left[1]})")
        print(f"Clicking at: ({click_x:.0f}, {click_y:.0f})")

        # Move cursor and click
        pyautogui.moveTo(click_x, click_y, duration=0.5)
        pyautogui.click()

        return True
    else:
        print(f"No match found above threshold {threshold}")
        return False

def find_all_matches(template_path, threshold=0.8, scale_factor=2):
    """
    Find all matches of template on screen (useful for debugging).
    """

    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path)
    if template is None:
        print(f"Error: Could not load template image from {template_path}")
        return []

    screenshot_gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    h, w = template_gray.shape
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find all matches above threshold
    locations = np.where(result >= threshold)
    matches = []

    for pt in zip(*locations[::-1]):
        center_x = (pt[0] + w // 2) / scale_factor
        center_y = (pt[1] + h // 2) / scale_factor
        confidence = result[pt[1], pt[0]]
        matches.append((center_x, center_y, confidence))

    return matches

# if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python script.py <template_image_path> [threshold] [scale_factor]")
    #     print("Example: python script.py button.png 0.8 2")
    #     sys.exit(1)
    #
template_path = 'images/altar.png'
threshold = .8
scale_factor = 2

print(f"Searching for template: {template_path}")
print(f"Threshold: {threshold}")
print(f"Scale factor: {scale_factor}")
print("-" * 50)

success = find_and_click_template(template_path, threshold, scale_factor)

if not success:
    print("\nTrying to find all matches for debugging...")
    matches = find_all_matches(template_path, threshold=0.5, scale_factor=scale_factor)
    print(f"Found {len(matches)} potential matches:")
    for i, (x, y, conf) in enumerate(matches[:5]):  # Show top 5
        print(f"  {i+1}. Position: ({x:.0f}, {y:.0f}), Confidence: {conf:.3f}")
