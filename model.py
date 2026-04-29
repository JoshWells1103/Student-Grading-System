def evaluate_student(exam, assessment, fee):
    exam_passed = exam >= 25
    assessment_passed = assessment >= 15

    req1= exam_passed and assessment_passed
    req2 = (exam == 25 and assessment == 14) or (exam == 24 and assessment == 15)
    
    is_qualified = req1 or req2

    if  is_qualified:
         status =  "Qualified"
         outcome = "Certificate Issued" if fee == 100 else "Certificate NOT issued"
    else:
        if not exam_passed and not assessment_passed:
              status = "FAILED"
              outcome = "Repeater (Failed both components)"
        else:
             status = "FAILED"
             outcome = "Failed to meet requirements"

    return {
        "exam_passed": exam_passed,
        "assessment_passed": assessment_passed,
        "status": status,
        "outcome": outcome
    }

