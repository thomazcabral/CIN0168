import pytest
from ScholarshipEligibilityEvaluator import evaluate_scholarship, Status

def teste_approved():
    resultado = evaluate_scholarship(age=20, gpa=9.0, attendance_rate=98.0, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.APPROVED
    assert "Applicant meets all scholarship requirements." in resultado.reasons

def teste_manual_review(): # manual review e caso de valor limite
    resultado = evaluate_scholarship(age=17, gpa=8.6, attendance_rate=95.5, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.MANUAL_REVIEW
    assert "Applicant is under 18 and requires manual review." in resultado.reasons

def teste_rejeicao_gpa():
    resultado = evaluate_scholarship(age=35, gpa=3.7, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.REJECTED
    assert "GPA is below the minimum required." in resultado.reasons

def teste_rejeicao_attendance_rate():
    resultado = evaluate_scholarship(age=40, gpa=8.7, attendance_rate=68.5, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.REJECTED
    assert "Attendance rate is below the minimum required." in resultado.reasons

def teste_rejeicao_has_required_courses():
    resultado = evaluate_scholarship(age=18, gpa=7.5, attendance_rate=97.7, has_required_courses=False, disciplinary_record=False)
    assert resultado.status == Status.REJECTED
    assert "Required courses have not been completed." in resultado.reasons

def teste_invalida_gpa():
    with pytest.raises(ValueError, match="GPA must be between 0 and 10."):
        evaluate_scholarship(age=25, gpa=14.8, attendance_rate=99.0, has_required_courses=True, disciplinary_record=False)

def teste_invalida_attendace_rate():
    with pytest.raises(ValueError, match="Attendance rate must be between 0 and 100."):
        evaluate_scholarship(age=30, gpa=8.9, attendance_rate=123.0, has_required_courses=True, disciplinary_record=False)

def teste_limite_age():
    resultado = evaluate_scholarship(age=16, gpa=7.9, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.MANUAL_REVIEW
    assert "Applicant is under 18 and requires manual review." in resultado.reasons

def teste_limite_gpa1():
    resultado = evaluate_scholarship(age=46, gpa=6.0, attendance_rate=88.8, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.MANUAL_REVIEW
    assert "GPA is in the manual review range." in resultado.reasons

def teste_limite_gpa2():
    resultado = evaluate_scholarship(age=55, gpa=7.0, attendance_rate=98.9, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.APPROVED
    assert "Applicant meets all scholarship requirements." in resultado.reasons

def teste_limite_attendance_rate1():
    resultado = evaluate_scholarship(age=22, gpa=8.5, attendance_rate=75.0, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.MANUAL_REVIEW
    assert "Attendance rate is in the manual review range." in resultado.reasons

def teste_limite_attendance_rate2():
    resultado = evaluate_scholarship(age=21, gpa=7.9, attendance_rate=80.0, has_required_courses=True, disciplinary_record=False)
    assert resultado.status == Status.APPROVED
    assert "Applicant meets all scholarship requirements." in resultado.reasons