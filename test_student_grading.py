from student_grading import calculate_average, assign_grade

# ---------------- GRADE S TEST CASES ----------------
def test_grade_s_lower_boundary():
    avg = calculate_average(90, 90, 90)
    assert assign_grade(avg) == "S"

def test_grade_s_middle_value():
    avg = calculate_average(95, 95, 95)
    assert assign_grade(avg) == "S"

def test_grade_s_upper_boundary():
    avg = calculate_average(100, 100, 100)
    assert assign_grade(avg) == "S"


# ---------------- GRADE A TEST CASES ----------------
def test_grade_a_lower_boundary():
    avg = calculate_average(80, 80, 80)
    assert assign_grade(avg) == "A"

def test_grade_a_middle_value():
    avg = calculate_average(85, 85, 85)
    assert assign_grade(avg) == "A"

def test_grade_a_upper_boundary():
    avg = calculate_average(89.99, 89.99, 89.99)
    assert assign_grade(avg) == "A"


# ---------------- GRADE B TEST CASES ----------------
def test_grade_b_lower_boundary():
    avg = calculate_average(65, 65, 65)
    assert assign_grade(avg) == "B"

def test_grade_b_middle_value():
    avg = calculate_average(70, 70, 70)
    assert assign_grade(avg) == "B"

def test_grade_b_upper_boundary():
    avg = calculate_average(79.99, 79.99, 79.99)
    assert assign_grade(avg) == "B"


# ---------------- GRADE C TEST CASES ----------------
def test_grade_c_lower_boundary():
    avg = calculate_average(50, 50, 50)
    assert assign_grade(avg) == "C"

def test_grade_c_middle_value():
    avg = calculate_average(55, 55, 55)
    assert assign_grade(avg) == "C"

def test_grade_c_upper_boundary():
    avg = calculate_average(64.99, 64.99, 64.99)
    assert assign_grade(avg) == "C"


# ---------------- GRADE D TEST CASES ----------------
def test_grade_d_lower_boundary():
    avg = calculate_average(40, 40, 40)
    assert assign_grade(avg) == "D"

def test_grade_d_middle_value():
    avg = calculate_average(45, 45, 45)
    assert assign_grade(avg) == "D"

def test_grade_d_upper_boundary():
    avg = calculate_average(49.99, 49.99, 49.99)
    assert assign_grade(avg) == "D"


# ---------------- GRADE F TEST CASE ----------------
def test_grade_f_below_40():
    avg = calculate_average(30, 35, 39)
    assert assign_grade(avg) == "F"
