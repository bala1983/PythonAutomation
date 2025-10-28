import pytest
from .db_infra import default_values
from .db_infra import show_student_by_name

@pytest.mark.db_test
def test_db_select():
    expected_result = "Інфо про студента Student 5: 5"
    default_values()
    actual_result = show_student_by_name('Student 5')
    assert actual_result == expected_result

