from model import evaluate_student

def main():
    print("--- Student Grading System ---")


    try:
        name = input("Enter Student Full Name: ")
        exam = int(input("Enter Exam Score: "))
        assess = int(input("Enter Assessment Score: "))
        fees = int(input("Enter Fee Paid: "))
    except ValueError:
        print("Error: Please enter numeric values for scores and fess.")
        return
    
   
    result = evaluate_student(exam, assess, fees)

  
    print(f"\n--- REPORT: {name.upper()} ---")
    print(f"Exam: {'Passed' if result['exam_passed'] else 'Failed'}") 
    print(f"Assessment: {'Passed' if result['assessment_passed'] else 'Failed'}")
    print(f"Status: {result['status']}")
    print(f"Outcome: {result['outcome']}")

if __name__ == "__main__":
    main()
