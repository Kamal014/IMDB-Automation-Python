import os
import shutil


def clean_allure_reports():
    report_dir = "../reports/allure-report"
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
        print(f"Allure report directory '{report_dir}' has been cleaned.")
    else:
        print(f"Directory '{report_dir}' does not exist.")


if __name__ == "__main__":
    clean_allure_reports()
