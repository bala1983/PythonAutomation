import pytest
import db_infra

@pytest.mark.db_test
def test_db_select():
    expected_result = "Інфо про студента Student 5: 5"
    db_infra.default_values()
    actual_result = db_infra.show_student_by_name('Student 5')
    assert actual_result == expected_result

