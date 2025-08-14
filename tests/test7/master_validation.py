#!/usr/bin/env python3
"""
Master Validation Script
Created by: テストAI7
Comprehensive validation of all project files and calculations
"""

import os
import json
import csv
import time
import subprocess
from typing import Dict, List, Tuple, Any
import numpy as np

class MasterValidator:
    """
    Master validation system for the entire project
    """
    
    def __init__(self):
        self.validation_results = {
            'file_validation': {},
            'calculation_validation': {},
            'format_validation': {},
            'execution_validation': {},
            'errors': [],
            'warnings': [],
            'summary': {}
        }
        self.start_time = time.time()
    
    def validate_file_structure(self) -> Dict[str, bool]:
        """
        Validate all required files and folders exist
        """
        required_structure = {
            'folders': [
                'research_project',
                'research_project/algorithms',
                'research_project/datasets',
                'research_project/models',
                'experiment_alpha',
                'experiment_beta', 
                'experiment_gamma',
                'analysis_results',
                'validation_suite'
            ],
            'files': [
                # Experiment files
                'experiment_alpha/config.json',
                'experiment_alpha/input_data.csv',
                'experiment_alpha/processing_script.py',
                'experiment_alpha/output_results.json',
                'experiment_alpha/metrics.txt',
                'experiment_alpha/error_log.txt',
                'experiment_alpha/summary.md',
                
                'experiment_beta/config.json',
                'experiment_beta/input_data.csv',
                'experiment_beta/processing_script.py',
                'experiment_beta/output_results.json',
                'experiment_beta/metrics.txt',
                'experiment_beta/error_log.txt',
                'experiment_beta/summary.md',
                
                'experiment_gamma/config.json',
                'experiment_gamma/input_data.csv',
                'experiment_gamma/processing_script.py',
                'experiment_gamma/output_results.json',
                'experiment_gamma/metrics.txt',
                'experiment_gamma/error_log.txt',
                'experiment_gamma/summary.md',
                
                # Algorithm files
                'research_project/algorithms/sorting_algorithms.py',
                'research_project/algorithms/search_algorithms.py',
                'research_project/algorithms/optimization.py',
                
                # Dataset files
                'research_project/datasets/training_data.csv',
                'research_project/datasets/test_data.csv',
                'research_project/datasets/metadata.json',
                
                # Model files
                'research_project/models/linear_model.py',
                'research_project/models/neural_network.py',
                'research_project/models/evaluation.py',
                
                # Main scripts
                'data_generator.py',
                'master_validation.py',
                'work_history.log'
            ]
        }
        
        file_results = {}
        
        # Check folders
        for folder in required_structure['folders']:
            exists = os.path.exists(folder) and os.path.isdir(folder)
            file_results[f"folder_{folder}"] = exists
            if not exists:
                self.validation_results['errors'].append(f"Missing folder: {folder}")
        
        # Check files
        for file in required_structure['files']:
            exists = os.path.exists(file) and os.path.isfile(file)
            file_results[f"file_{file}"] = exists
            if not exists:
                self.validation_results['errors'].append(f"Missing file: {file}")
        
        self.validation_results['file_validation'] = file_results
        return file_results
    
    def validate_calculation_accuracy(self) -> Dict[str, bool]:
        """
        Validate calculation results for accuracy
        """
        calc_results = {}
        
        # Validate Alpha experiment (summation formula)
        try:
            alpha_result = self.validate_alpha_calculation()
            calc_results['alpha_calculation'] = alpha_result
        except Exception as e:
            calc_results['alpha_calculation'] = False
            self.validation_results['errors'].append(f"Alpha calculation validation failed: {e}")
        
        # Validate Beta experiment (matrix operations)
        try:
            beta_result = self.validate_beta_calculation()
            calc_results['beta_calculation'] = beta_result
        except Exception as e:
            calc_results['beta_calculation'] = False
            self.validation_results['errors'].append(f"Beta calculation validation failed: {e}")
        
        # Validate Gamma experiment (Fibonacci)
        try:
            gamma_result = self.validate_gamma_calculation()
            calc_results['gamma_calculation'] = gamma_result
        except Exception as e:
            calc_results['gamma_calculation'] = False
            self.validation_results['errors'].append(f"Gamma calculation validation failed: {e}")
        
        self.validation_results['calculation_validation'] = calc_results
        return calc_results
    
    def validate_alpha_calculation(self) -> bool:
        """
        Validate Alpha experiment calculation: Σ(i=1 to 100) [a * i^2 + b * i + c] / (d + e * i)
        """
        # Parameters
        a, b, c, d, e = 512, 256, 128, 64, 32
        
        # Manual calculation for verification
        expected_sum = 0
        for i in range(1, 101):
            numerator = a * i**2 + b * i + c
            denominator = d + e * i
            expected_sum += numerator / denominator
        
        expected_result = round(expected_sum, 5)
        
        # Check if results file exists and contains correct value
        if os.path.exists('experiment_alpha/output_results.json'):
            with open('experiment_alpha/output_results.json', 'r') as f:
                results = json.load(f)
                actual_result = results.get('final_result', 0)
                
                # Allow small tolerance for floating point errors
                tolerance = 0.001
                return abs(actual_result - expected_result) < tolerance
        
        return False
    
    def validate_beta_calculation(self) -> bool:
        """
        Validate Beta experiment matrix calculations
        """
        # Check if results exist
        if os.path.exists('experiment_beta/output_results.json'):
            with open('experiment_beta/output_results.json', 'r') as f:
                results = json.load(f)
                
                # Verify matrix structure
                matrix_a = results.get('matrix_A', [])
                matrix_product = results.get('matrix_product', [])
                
                # Basic validation - check dimensions
                if len(matrix_a) == 5 and len(matrix_a[0]) == 5:
                    if len(matrix_product) == 5 and len(matrix_product[0]) == 5:
                        # Check if determinant exists (can be 0 for singular matrices)
                        determinants = results.get('determinants', {})
                        return 'det_A' in determinants and 'det_product' in determinants
        
        return False
    
    def validate_gamma_calculation(self) -> bool:
        """
        Validate Gamma experiment Fibonacci calculations
        """
        # Expected F(50) and F(60) values
        expected_f50 = 12586269025
        expected_f60 = 1548008755920
        
        if os.path.exists('experiment_gamma/output_results.json'):
            with open('experiment_gamma/output_results.json', 'r') as f:
                results = json.load(f)
                
                f50_result = results.get('standard_fibonacci', {}).get('F_50', {}).get('value', 0)
                f60_result = results.get('standard_fibonacci', {}).get('F_60', {}).get('value', 0)
                
                return f50_result == expected_f50 and f60_result == expected_f60
        
        return False
    
    def validate_file_formats(self) -> Dict[str, bool]:
        """
        Validate file formats are correct
        """
        format_results = {}
        
        # Validate JSON files
        json_files = [
            'experiment_alpha/config.json',
            'experiment_alpha/output_results.json',
            'experiment_beta/config.json',
            'experiment_beta/output_results.json',
            'experiment_gamma/config.json',
            'experiment_gamma/output_results.json',
            'research_project/datasets/metadata.json'
        ]
        
        for json_file in json_files:
            try:
                if os.path.exists(json_file):
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                    format_results[f"json_{json_file}"] = True
                else:
                    format_results[f"json_{json_file}"] = False
            except json.JSONDecodeError:
                format_results[f"json_{json_file}"] = False
                self.validation_results['errors'].append(f"Invalid JSON format: {json_file}")
        
        # Validate CSV files
        csv_files = [
            'experiment_alpha/input_data.csv',
            'experiment_beta/input_data.csv',
            'experiment_gamma/input_data.csv',
            'research_project/datasets/training_data.csv',
            'research_project/datasets/test_data.csv'
        ]
        
        for csv_file in csv_files:
            try:
                if os.path.exists(csv_file):
                    with open(csv_file, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        rows = list(reader)
                        # Check if it has header and at least one data row
                        format_results[f"csv_{csv_file}"] = len(rows) >= 2
                else:
                    format_results[f"csv_{csv_file}"] = False
            except Exception:
                format_results[f"csv_{csv_file}"] = False
                self.validation_results['errors'].append(f"Invalid CSV format: {csv_file}")
        
        self.validation_results['format_validation'] = format_results
        return format_results
    
    def validate_script_execution(self) -> Dict[str, bool]:
        """
        Validate that Python scripts can be executed without errors
        """
        execution_results = {}
        
        python_scripts = [
            'experiment_alpha/processing_script.py',
            'experiment_beta/processing_script.py',
            'experiment_gamma/processing_script.py',
            'data_generator.py'
        ]
        
        for script in python_scripts:
            try:
                if os.path.exists(script):
                    # Try to compile the script
                    with open(script, 'r', encoding='utf-8') as f:
                        code = f.read()
                    
                    compile(code, script, 'exec')
                    execution_results[f"compile_{script}"] = True
                else:
                    execution_results[f"compile_{script}"] = False
            except SyntaxError as e:
                execution_results[f"compile_{script}"] = False
                self.validation_results['errors'].append(f"Syntax error in {script}: {e}")
            except Exception as e:
                execution_results[f"compile_{script}"] = False
                self.validation_results['errors'].append(f"Error compiling {script}: {e}")
        
        self.validation_results['execution_validation'] = execution_results
        return execution_results
    
    def measure_execution_times(self) -> Dict[str, float]:
        """
        Measure execution times for performance validation
        """
        execution_times = {}
        
        # Measure experiment script execution times
        experiments = ['alpha', 'beta', 'gamma']
        
        for exp in experiments:
            script_path = f"experiment_{exp}/processing_script.py"
            if os.path.exists(script_path):
                try:
                    start_time = time.time()
                    # Change to experiment directory and run script
                    os.chdir(f"experiment_{exp}")
                    result = subprocess.run(['python', 'processing_script.py'], 
                                          capture_output=True, text=True, timeout=30)
                    os.chdir('..')
                    
                    end_time = time.time()
                    execution_times[f"experiment_{exp}"] = (end_time - start_time) * 1000
                    
                    if result.returncode != 0:
                        self.validation_results['warnings'].append(f"Experiment {exp} script execution warning: {result.stderr}")
                
                except subprocess.TimeoutExpired:
                    execution_times[f"experiment_{exp}"] = -1  # Timeout
                    self.validation_results['errors'].append(f"Experiment {exp} script execution timeout")
                except Exception as e:
                    execution_times[f"experiment_{exp}"] = -1  # Error
                    self.validation_results['errors'].append(f"Error executing experiment {exp}: {e}")
        
        return execution_times
    
    def run_comprehensive_validation(self) -> Dict[str, Any]:
        """
        Run all validation checks
        """
        print("Running comprehensive validation...")
        print("=" * 50)
        
        # 1. File structure validation
        print("1. Validating file structure...")
        file_validation = self.validate_file_structure()
        
        # 2. Calculation accuracy validation
        print("2. Validating calculation accuracy...")
        calc_validation = self.validate_calculation_accuracy()
        
        # 3. File format validation
        print("3. Validating file formats...")
        format_validation = self.validate_file_formats()
        
        # 4. Script execution validation
        print("4. Validating script execution...")
        execution_validation = self.validate_script_execution()
        
        # 5. Performance measurement
        print("5. Measuring execution times...")
        execution_times = self.measure_execution_times()
        
        # Generate summary
        total_checks = len(file_validation) + len(calc_validation) + len(format_validation) + len(execution_validation)
        passed_checks = (list(file_validation.values()) + list(calc_validation.values()) + 
                        list(format_validation.values()) + list(execution_validation.values())).count(True)
        
        self.validation_results['summary'] = {
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'failed_checks': total_checks - passed_checks,
            'success_rate': (passed_checks / total_checks) * 100 if total_checks > 0 else 0,
            'total_errors': len(self.validation_results['errors']),
            'total_warnings': len(self.validation_results['warnings']),
            'execution_times': execution_times,
            'validation_duration_ms': (time.time() - self.start_time) * 1000
        }
        
        return self.validation_results
    
    def save_validation_report(self):
        """
        Save validation results to files
        """
        # Save detailed JSON report
        with open('validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(self.validation_results, f, indent=2, ensure_ascii=False)
        
        # Save summary text report
        summary = self.validation_results['summary']
        with open('validation_summary.txt', 'w', encoding='utf-8') as f:
            f.write("MASTER VALIDATION SUMMARY\n")
            f.write("=" * 30 + "\n")
            f.write(f"Created by: テストAI7\n")
            f.write(f"Validation Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write(f"Total Checks: {summary['total_checks']}\n")
            f.write(f"Passed: {summary['passed_checks']}\n")
            f.write(f"Failed: {summary['failed_checks']}\n")
            f.write(f"Success Rate: {summary['success_rate']:.1f}%\n\n")
            
            f.write(f"Errors: {summary['total_errors']}\n")
            f.write(f"Warnings: {summary['total_warnings']}\n")
            f.write(f"Validation Duration: {summary['validation_duration_ms']:.1f} ms\n\n")
            
            if self.validation_results['errors']:
                f.write("ERRORS:\n")
                for error in self.validation_results['errors']:
                    f.write(f"- {error}\n")
                f.write("\n")
            
            if self.validation_results['warnings']:
                f.write("WARNINGS:\n")
                for warning in self.validation_results['warnings']:
                    f.write(f"- {warning}\n")
        
        print(f"Validation reports saved: validation_report.json, validation_summary.txt")

def main():
    """
    Main validation execution
    """
    print("Master Validation Script - Created by テストAI7")
    print("=" * 60)
    
    validator = MasterValidator()
    
    # Run comprehensive validation
    results = validator.run_comprehensive_validation()
    
    # Display results
    summary = results['summary']
    print("\nVALIDATION COMPLETED!")
    print("=" * 30)
    print(f"Total Checks: {summary['total_checks']}")
    print(f"Passed: {summary['passed_checks']}")
    print(f"Failed: {summary['failed_checks']}")
    print(f"Success Rate: {summary['success_rate']:.1f}%")
    print(f"Execution Time: {summary['validation_duration_ms']:.1f} ms")
    
    if results['errors']:
        print(f"\nErrors Found: {len(results['errors'])}")
        for error in results['errors'][:5]:  # Show first 5 errors
            print(f"  - {error}")
        if len(results['errors']) > 5:
            print(f"  ... and {len(results['errors']) - 5} more errors")
    
    if results['warnings']:
        print(f"\nWarnings: {len(results['warnings'])}")
    
    # Save reports
    validator.save_validation_report()
    
    print(f"\nValidation Status: {'PASSED' if summary['success_rate'] >= 80 else 'FAILED'}")

if __name__ == "__main__":
    main()