import pytesseract
from PIL import Image
import pandas as pd
import difflib
import cv2

medicine_data = pd.read_csv('E:\\A_Z_medicines_dataset_of_India.csv')

def ocr_extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    blur = cv2.GaussianBlur(equ, (5, 5), 0)
    text = pytesseract.image_to_string(blur)
    return text

def find_alternative_medicines(prescribed_medicine, medicine_data):
    matching_medicines = difflib.get_close_matches(prescribed_medicine, medicine_data['name'])
    return matching_medicines

def display_medicine_details(medicine_name, medicine_data):
    matching_medicines = medicine_data[medicine_data['name'] == medicine_name]
    if not matching_medicines.empty:
        medicine_info = matching_medicines.iloc[0]
        print("Product Name:", medicine_info['name'])
        print("Price:", medicine_info['price(₹)'])
        print("Manufacturer:", medicine_info['manufacturer_name'])
        print("Composition:", medicine_info['short_composition1'], medicine_info['short_composition2'])
        print("\n")
    else:
        print("Entered medicine '{}' not found in the database.".format(medicine_name))

def display_alternative_medicines(alternatives, medicine_data):
    for med in alternatives:
        medicine_info = medicine_data[medicine_data['name'] == med].iloc[0]
        print("Alternative Product Name:", medicine_info['name'])
        print("Price:", medicine_info['price(₹)'])
        print("Manufacturer:", medicine_info['manufacturer_name'])
        print("Composition:", medicine_info['short_composition1'], medicine_info['short_composition2'])
        print("\n")

def get_user_input():
    choice = input("Enter '1' to enter the name of the medicine or '2' to upload a prescription image: ")
    if choice == '1':
        prescribed_medicines = input("Enter the names of the prescribed medicines separated by commas: ").split(',')
        return prescribed_medicines
    elif choice == '2':
        prescription_image_path = input("Enter the path to the prescription image: ").strip('"')
        prescription_text = ocr_extract_text(prescription_image_path)
        prescribed_medicines = [medicine.strip() for medicine in prescription_text.split('\n') if medicine.strip()]
        return prescribed_medicines
    else:
        print("Invalid choice.")
        return None

def main():
    user_input = get_user_input()
    if user_input:
        for prescribed_medicine in user_input:
            if prescribed_medicine.endswith('.jpg') or prescribed_medicine.endswith('.png'):
                prescribed_medicine = ocr_extract_text(prescribed_medicine)
            alternatives = find_alternative_medicines(prescribed_medicine, medicine_data)
            if alternatives:
                print("\n\nDetails of the Entered Medicine:")
                display_medicine_details(prescribed_medicine, medicine_data)
                print("\n\nAlternative Medicines:")
                display_alternative_medicines(alternatives, medicine_data)
            else:
                print("No alternative medicines found for '{}'.".format(prescribed_medicine))

if __name__ == "__main__":
    main()
