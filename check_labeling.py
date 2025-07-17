import cv2
import xml.etree.ElementTree as ET
import random
import os

def parse_voc_xml(xml_file):
    """Parse Pascal VOC XML file and extract bounding box information"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    boxes = []
    for obj in root.findall('object'):
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        
        boxes.append({
            'name': name,
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax
        })
    
    return boxes

def draw_bounding_boxes(image_path, xml_path, output_path=None):
    """Draw bounding boxes on image using Pascal VOC XML annotations"""
    
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return
    
    # Parse XML file
    try:
        boxes = parse_voc_xml(xml_path)
    except Exception as e:
        print(f"Error parsing XML file: {e}")
        return
    
    # Draw bounding boxes
    for box in boxes:
        # Generate random color for each box
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Draw rectangle
        cv2.rectangle(image, 
                     (box['xmin'], box['ymin']), 
                     (box['xmax'], box['ymax']), 
                     color, 2)
        
        # Draw label
        label = box['name']
        label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
        
        # Draw label background
        cv2.rectangle(image, 
                     (box['xmin'], box['ymin'] - label_size[1] - 10),
                     (box['xmin'] + label_size[0], box['ymin']),
                     color, -1)
        
        # Draw label text
        cv2.putText(image, label, 
                   (box['xmin'], box['ymin'] - 5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    # Save or display result
    if output_path:
        success = cv2.imwrite(output_path, image)
        if success:
            print(f"Output saved to {output_path}")
            print(f"Full path: {os.path.abspath(output_path)}")
        else:
            print(f"Error: Failed to save image to {output_path}")
    else:
        cv2.imshow('Image with Bounding Boxes', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    # Replace with your file paths
    image_path = "/home/nvidia/Finalproject/test_img_renamed/10000.jpg"
    xml_path = "/home/nvidia/Finalproject/test_xml_renamed/10000.xml"
    output_path = "/home/nvidia/Finalproject/output.jpg"  # Use full path
    
    draw_bounding_boxes(image_path, xml_path, output_path)