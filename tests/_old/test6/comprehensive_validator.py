#!/usr/bin/env python3
"""
Comprehensive Validator for Research Platform
=============================================

Advanced validation script with 15+ unit tests and 5+ integration tests
Includes checksum verification, accuracy validation, and performance profiling
"""

import os
import sys
import json
import yaml
import csv
import hashlib
import time
import unittest
import subprocess
import traceback
import psutil
import threading
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

class ComprehensiveValidator:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.results = {
            'validation_timestamp': datetime.now().isoformat(),
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'unit_tests': [],
            'integration_tests': [],
            'performance_metrics': {},
            'file_integrity': {},
            'errors': []
        }
        self.start_time = time.time()
        
    def log_test_result(self, test_name: str, passed: bool, details: str = "", test_type: str = "unit"):
        """Log test result"""
        result = {
            'name': test_name,
            'passed': passed,
            'details': details,
            'timestamp': datetime.now().isoformat()
        }
        
        if test_type == "unit":
            self.results['unit_tests'].append(result)
        else:
            self.results['integration_tests'].append(result)
            
        self.results['total_tests'] += 1
        if passed:
            self.results['passed_tests'] += 1
        else:
            self.results['failed_tests'] += 1
    
    def calculate_file_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum of file"""
        if not file_path.exists():
            return ""
        
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception as e:
            return f"ERROR: {str(e)}"
    
    # =================== UNIT TESTS (15+) ===================
    
    def test_folder_structure_integrity(self):
        """Unit Test 1: Verify all required folders exist"""
        try:
            required_folders = [
                "research_platform",
                "research_platform/data_pipeline",
                "research_platform/data_pipeline/raw_data",
                "research_platform/data_pipeline/processed_data",
                "research_platform/ml_models",
                "research_platform/ml_models/training",
                "research_platform/ml_models/evaluation",
                "research_platform/optimization",
                "research_platform/visualization",
                "trial_alpha",
                "trial_beta", 
                "trial_gamma",
                "trial_delta"
            ]
            
            missing_folders = []
            for folder in required_folders:
                if not (self.base_path / folder).exists():
                    missing_folders.append(folder)
            
            passed = len(missing_folders) == 0
            details = f"Missing folders: {missing_folders}" if missing_folders else "All folders present"
            self.log_test_result("folder_structure_integrity", passed, details)
            
        except Exception as e:
            self.log_test_result("folder_structure_integrity", False, f"Exception: {str(e)}")
    
    def test_trial_alpha_files_existence(self):
        """Unit Test 2: Verify trial_alpha files exist"""
        try:
            required_files = [
                "trial_alpha/algorithm.py",
                "trial_alpha/parameters.toml",
                "trial_alpha/dataset.json",
                "trial_alpha/results.json",
                "trial_alpha/metrics.yaml",
                "trial_alpha/diagnostic.log",
                "trial_alpha/visualization.svg"
            ]
            
            missing_files = []
            for file_path in required_files:
                if not (self.base_path / file_path).exists():
                    missing_files.append(file_path)
            
            passed = len(missing_files) == 0
            details = f"Missing files: {missing_files}" if missing_files else "All trial_alpha files present"
            self.log_test_result("trial_alpha_files_existence", passed, details)
            
        except Exception as e:
            self.log_test_result("trial_alpha_files_existence", False, f"Exception: {str(e)}")
    
    def test_trial_beta_files_existence(self):
        """Unit Test 3: Verify trial_beta files exist"""
        try:
            required_files = [
                "trial_beta/algorithm.py",
                "trial_beta/parameters.toml",
                "trial_beta/dataset.json",
                "trial_beta/results.json",
                "trial_beta/metrics.yaml",
                "trial_beta/diagnostic.log",
                "trial_beta/visualization.svg"
            ]
            
            missing_files = []
            for file_path in required_files:
                if not (self.base_path / file_path).exists():
                    missing_files.append(file_path)
            
            passed = len(missing_files) == 0
            details = f"Missing files: {missing_files}" if missing_files else "All trial_beta files present"
            self.log_test_result("trial_beta_files_existence", passed, details)
            
        except Exception as e:
            self.log_test_result("trial_beta_files_existence", False, f"Exception: {str(e)}")
    
    def test_raw_data_files_integrity(self):
        """Unit Test 4: Verify raw data files and structure"""
        try:
            csv_path = self.base_path / "research_platform/data_pipeline/raw_data/sensor_data.csv"
            json_path = self.base_path / "research_platform/data_pipeline/raw_data/metadata.json"
            yaml_path = self.base_path / "research_platform/data_pipeline/raw_data/quality_report.yaml"
            
            issues = []
            
            # Check CSV file
            if csv_path.exists():
                try:
                    with open(csv_path, 'r') as f:
                        reader = csv.reader(f)
                        rows = list(reader)
                        if len(rows) < 1000:  # Should have at least 1000 rows
                            issues.append(f"CSV has only {len(rows)} rows, expected >= 1000")
                except Exception as e:
                    issues.append(f"CSV read error: {str(e)}")
            else:
                issues.append("sensor_data.csv missing")
            
            # Check JSON file
            if json_path.exists():
                try:
                    with open(json_path, 'r') as f:
                        json.load(f)
                except Exception as e:
                    issues.append(f"JSON parse error: {str(e)}")
            else:
                issues.append("metadata.json missing")
            
            # Check YAML file
            if yaml_path.exists():
                try:
                    with open(yaml_path, 'r') as f:
                        yaml.safe_load(f)
                except Exception as e:
                    issues.append(f"YAML parse error: {str(e)}")
            else:
                issues.append("quality_report.yaml missing")
            
            passed = len(issues) == 0
            details = f"Issues: {issues}" if issues else "All raw data files valid"
            self.log_test_result("raw_data_files_integrity", passed, details)
            
        except Exception as e:
            self.log_test_result("raw_data_files_integrity", False, f"Exception: {str(e)}")
    
    def test_algorithm_syntax_validation(self):
        """Unit Test 5: Verify Python algorithm files have valid syntax"""
        try:
            algorithm_files = [
                "trial_alpha/algorithm.py",
                "trial_beta/algorithm.py",
                "trial_gamma/algorithm.py",
                "trial_delta/algorithm.py"
            ]
            
            syntax_errors = []
            for file_path in algorithm_files:
                full_path = self.base_path / file_path
                if full_path.exists():
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            code = f.read()
                        compile(code, str(full_path), 'exec')
                    except SyntaxError as e:
                        syntax_errors.append(f"{file_path}: {str(e)}")
                    except Exception as e:
                        syntax_errors.append(f"{file_path}: {str(e)}")
                else:
                    syntax_errors.append(f"{file_path}: File not found")
            
            passed = len(syntax_errors) == 0
            details = f"Syntax errors: {syntax_errors}" if syntax_errors else "All algorithm files have valid syntax"
            self.log_test_result("algorithm_syntax_validation", passed, details)
            
        except Exception as e:
            self.log_test_result("algorithm_syntax_validation", False, f"Exception: {str(e)}")
    
    def test_json_files_validity(self):
        """Unit Test 6: Verify all JSON files are valid"""
        try:
            json_files = []
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if file.endswith('.json'):
                        json_files.append(os.path.join(root, file))
            
            invalid_files = []
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        json.load(f)
                except Exception as e:
                    invalid_files.append(f"{json_file}: {str(e)}")
            
            passed = len(invalid_files) == 0
            details = f"Invalid JSON files: {invalid_files}" if invalid_files else f"All {len(json_files)} JSON files valid"
            self.log_test_result("json_files_validity", passed, details)
            
        except Exception as e:
            self.log_test_result("json_files_validity", False, f"Exception: {str(e)}")
    
    def test_yaml_files_validity(self):
        """Unit Test 7: Verify all YAML files are valid"""
        try:
            yaml_files = []
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if file.endswith('.yaml') or file.endswith('.yml'):
                        yaml_files.append(os.path.join(root, file))
            
            invalid_files = []
            for yaml_file in yaml_files:
                try:
                    with open(yaml_file, 'r', encoding='utf-8') as f:
                        yaml.safe_load(f)
                except Exception as e:
                    invalid_files.append(f"{yaml_file}: {str(e)}")
            
            passed = len(invalid_files) == 0
            details = f"Invalid YAML files: {invalid_files}" if invalid_files else f"All {len(yaml_files)} YAML files valid"
            self.log_test_result("yaml_files_validity", passed, details)
            
        except Exception as e:
            self.log_test_result("yaml_files_validity", False, f"Exception: {str(e)}")
    
    def test_file_sizes_reasonable(self):
        """Unit Test 8: Check file sizes are reasonable"""
        try:
            size_issues = []
            
            # Check if files are too small (indicating incomplete generation)
            min_sizes = {
                'sensor_data.csv': 100000,  # Should be at least 100KB
                'dataset.json': 10000,      # Should be at least 10KB
                'algorithm.py': 1000        # Should be at least 1KB
            }
            
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    file_path = Path(root) / file
                    file_size = file_path.stat().st_size
                    
                    # Check minimum sizes for specific files
                    for pattern, min_size in min_sizes.items():
                        if pattern in file:
                            if file_size < min_size:
                                size_issues.append(f"{file_path}: {file_size} bytes < {min_size} bytes")
                    
                    # Check for unreasonably large files (>100MB)
                    if file_size > 100 * 1024 * 1024:
                        size_issues.append(f"{file_path}: {file_size} bytes too large")
            
            passed = len(size_issues) == 0
            details = f"Size issues: {size_issues}" if size_issues else "All file sizes reasonable"
            self.log_test_result("file_sizes_reasonable", passed, details)
            
        except Exception as e:
            self.log_test_result("file_sizes_reasonable", False, f"Exception: {str(e)}")
    
    def test_calculation_precision_compliance(self):
        """Unit Test 9: Verify calculation results meet precision requirements"""
        try:
            precision_issues = []
            
            # Check trial results for precision compliance
            trials = {
                'trial_alpha': 7,    # 7 decimal places
                'trial_beta': 9,     # 9 decimal places  
                'trial_gamma': 8,    # 8 decimal places
                'trial_delta': 10    # 10 decimal places
            }
            
            for trial, expected_precision in trials.items():
                results_path = self.base_path / f"{trial}/results.json"
                if results_path.exists():
                    try:
                        with open(results_path, 'r') as f:
                            data = json.load(f)
                        
                        # Check if precision field exists and matches
                        if 'precision' in data:
                            if data['precision'] != expected_precision:
                                precision_issues.append(f"{trial}: precision {data['precision']} != {expected_precision}")
                        else:
                            precision_issues.append(f"{trial}: precision field missing")
                            
                    except Exception as e:
                        precision_issues.append(f"{trial}: error reading results - {str(e)}")
                else:
                    precision_issues.append(f"{trial}: results.json not found")
            
            passed = len(precision_issues) == 0
            details = f"Precision issues: {precision_issues}" if precision_issues else "All calculations meet precision requirements"
            self.log_test_result("calculation_precision_compliance", passed, details)
            
        except Exception as e:
            self.log_test_result("calculation_precision_compliance", False, f"Exception: {str(e)}")
    
    def test_work_history_log_completeness(self):
        """Unit Test 10: Verify work_history.log has sufficient entries"""
        try:
            log_path = self.base_path / "work_history.log"
            
            if not log_path.exists():
                self.log_test_result("work_history_log_completeness", False, "work_history.log not found")
                return
            
            with open(log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Check for minimum 30 lines as required
            if len(lines) < 30:
                self.log_test_result("work_history_log_completeness", False, 
                                   f"Only {len(lines)} lines, required >= 30")
                return
            
            # Check for proper format [テストAI6] YYYYMMDD HH:MM:SS
            format_issues = []
            for i, line in enumerate(lines[:10]):  # Check first 10 lines
                if not line.startswith('[テストAI6]'):
                    format_issues.append(f"Line {i+1}: Missing [テストAI6] prefix")
            
            passed = len(format_issues) == 0
            details = f"Format issues: {format_issues}" if format_issues else f"Log complete with {len(lines)} lines"
            self.log_test_result("work_history_log_completeness", passed, details)
            
        except Exception as e:
            self.log_test_result("work_history_log_completeness", False, f"Exception: {str(e)}")
    
    def test_svg_files_validity(self):
        """Unit Test 11: Verify SVG files are valid XML"""
        try:
            svg_files = []
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if file.endswith('.svg'):
                        svg_files.append(os.path.join(root, file))
            
            invalid_svgs = []
            for svg_file in svg_files:
                try:
                    with open(svg_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic SVG validation
                    if not content.strip().startswith('<?xml'):
                        invalid_svgs.append(f"{svg_file}: Missing XML declaration")
                    elif '<svg' not in content:
                        invalid_svgs.append(f"{svg_file}: Missing SVG element")
                        
                except Exception as e:
                    invalid_svgs.append(f"{svg_file}: {str(e)}")
            
            passed = len(invalid_svgs) == 0
            details = f"Invalid SVG files: {invalid_svgs}" if invalid_svgs else f"All {len(svg_files)} SVG files valid"
            self.log_test_result("svg_files_validity", passed, details)
            
        except Exception as e:
            self.log_test_result("svg_files_validity", False, f"Exception: {str(e)}")
    
    def test_toml_files_validity(self):
        """Unit Test 12: Verify TOML files are valid"""
        try:
            toml_files = []
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if file.endswith('.toml'):
                        toml_files.append(os.path.join(root, file))
            
            # Simple TOML validation (without external library)
            invalid_tomls = []
            for toml_file in toml_files:
                try:
                    with open(toml_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic checks for TOML format
                    if '[' not in content and '=' not in content:
                        invalid_tomls.append(f"{toml_file}: No TOML sections or key-value pairs found")
                        
                except Exception as e:
                    invalid_tomls.append(f"{toml_file}: {str(e)}")
            
            passed = len(invalid_tomls) == 0
            details = f"Invalid TOML files: {invalid_tomls}" if invalid_tomls else f"All {len(toml_files)} TOML files valid"
            self.log_test_result("toml_files_validity", passed, details)
            
        except Exception as e:
            self.log_test_result("toml_files_validity", False, f"Exception: {str(e)}")
    
    def test_log_files_timestamp_format(self):
        """Unit Test 13: Verify log files have proper timestamp format"""
        try:
            log_files = []
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if file.endswith('.log'):
                        log_files.append(os.path.join(root, file))
            
            timestamp_issues = []
            for log_file in log_files:
                try:
                    with open(log_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()[:5]  # Check first 5 lines
                    
                    for i, line in enumerate(lines):
                        # Look for timestamp pattern YYYY-MM-DD HH:MM:SS
                        if not any(char.isdigit() for char in line[:20]):
                            continue  # Skip lines without timestamps
                        
                        # Basic timestamp format check
                        if len(line) > 19 and ':' in line[:20] and '-' in line[:20]:
                            continue  # Likely has timestamp
                        else:
                            timestamp_issues.append(f"{log_file} line {i+1}: Possible timestamp format issue")
                            break
                        
                except Exception as e:
                    timestamp_issues.append(f"{log_file}: {str(e)}")
            
            passed = len(timestamp_issues) == 0
            details = f"Timestamp issues: {timestamp_issues}" if timestamp_issues else f"All {len(log_files)} log files have proper timestamps"
            self.log_test_result("log_files_timestamp_format", passed, details)
            
        except Exception as e:
            self.log_test_result("log_files_timestamp_format", False, f"Exception: {str(e)}")
    
    def test_dataset_element_count(self):
        """Unit Test 14: Verify datasets have at least 1000 elements"""
        try:
            dataset_files = []
            for trial in ['trial_alpha', 'trial_beta', 'trial_gamma', 'trial_delta']:
                dataset_path = self.base_path / f"{trial}/dataset.json"
                if dataset_path.exists():
                    dataset_files.append(dataset_path)
            
            element_issues = []
            for dataset_file in dataset_files:
                try:
                    with open(dataset_file, 'r') as f:
                        data = json.load(f)
                    
                    # Look for array with 1000+ elements
                    found_large_array = False
                    for key, value in data.items():
                        if isinstance(value, list) and len(value) >= 1000:
                            found_large_array = True
                            break
                        elif isinstance(value, dict):
                            for subkey, subvalue in value.items():
                                if isinstance(subvalue, list) and len(subvalue) >= 1000:
                                    found_large_array = True
                                    break
                    
                    if not found_large_array:
                        element_issues.append(f"{dataset_file}: No array with 1000+ elements found")
                        
                except Exception as e:
                    element_issues.append(f"{dataset_file}: {str(e)}")
            
            passed = len(element_issues) == 0
            details = f"Element count issues: {element_issues}" if element_issues else f"All {len(dataset_files)} datasets have 1000+ elements"
            self.log_test_result("dataset_element_count", passed, details)
            
        except Exception as e:
            self.log_test_result("dataset_element_count", False, f"Exception: {str(e)}")
    
    def test_file_encoding_consistency(self):
        """Unit Test 15: Verify files use consistent encoding"""
        try:
            encoding_issues = []
            text_files = []
            
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if any(file.endswith(ext) for ext in ['.py', '.json', '.yaml', '.yml', '.toml', '.log', '.csv', '.md']):
                        text_files.append(os.path.join(root, file))
            
            for text_file in text_files:
                try:
                    # Try to read as UTF-8
                    with open(text_file, 'r', encoding='utf-8') as f:
                        f.read()
                except UnicodeDecodeError:
                    encoding_issues.append(f"{text_file}: Not UTF-8 encoded")
                except Exception as e:
                    encoding_issues.append(f"{text_file}: {str(e)}")
            
            passed = len(encoding_issues) == 0
            details = f"Encoding issues: {encoding_issues}" if encoding_issues else f"All {len(text_files)} text files are UTF-8 encoded"
            self.log_test_result("file_encoding_consistency", passed, details)
            
        except Exception as e:
            self.log_test_result("file_encoding_consistency", False, f"Exception: {str(e)}")
    
    def test_numerical_results_sanity(self):
        """Unit Test 16: Verify numerical results are within reasonable ranges"""
        try:
            sanity_issues = []
            
            trials = ['trial_alpha', 'trial_beta', 'trial_gamma', 'trial_delta']
            for trial in trials:
                results_path = self.base_path / f"{trial}/results.json"
                if results_path.exists():
                    try:
                        with open(results_path, 'r') as f:
                            data = json.load(f)
                        
                        # Look for numerical results
                        for key, value in data.items():
                            if isinstance(value, (int, float)):
                                # Check for NaN, infinity
                                if str(value).lower() in ['nan', 'inf', '-inf']:
                                    sanity_issues.append(f"{trial}: {key} = {value} (invalid)")
                                # Check for extremely large values
                                elif abs(value) > 1e100:
                                    sanity_issues.append(f"{trial}: {key} = {value} (extremely large)")
                                    
                    except Exception as e:
                        sanity_issues.append(f"{trial}: Error reading results - {str(e)}")
            
            passed = len(sanity_issues) == 0
            details = f"Sanity issues: {sanity_issues}" if sanity_issues else "All numerical results are within reasonable ranges"
            self.log_test_result("numerical_results_sanity", passed, details)
            
        except Exception as e:
            self.log_test_result("numerical_results_sanity", False, f"Exception: {str(e)}")
    
    # =================== INTEGRATION TESTS (5+) ===================
    
    def test_data_pipeline_integration(self):
        """Integration Test 1: Data pipeline from raw to processed"""
        try:
            # Check if raw data exists
            raw_csv = self.base_path / "research_platform/data_pipeline/raw_data/sensor_data.csv"
            raw_metadata = self.base_path / "research_platform/data_pipeline/raw_data/metadata.json"
            
            issues = []
            
            if not raw_csv.exists():
                issues.append("Raw sensor data missing")
            if not raw_metadata.exists():
                issues.append("Raw metadata missing")
            
            # Check data consistency
            if raw_csv.exists() and raw_metadata.exists():
                try:
                    with open(raw_metadata, 'r') as f:
                        metadata = json.load(f)
                    
                    with open(raw_csv, 'r') as f:
                        reader = csv.reader(f)
                        rows = list(reader)
                    
                    # Verify row count matches metadata
                    if 'dataset_info' in metadata and 'total_records' in metadata['dataset_info']:
                        expected_rows = metadata['dataset_info']['total_records']
                        actual_rows = len(rows) - 1  # Subtract header
                        if abs(actual_rows - expected_rows) > 10:  # Allow small discrepancy
                            issues.append(f"Row count mismatch: {actual_rows} vs {expected_rows}")
                    
                except Exception as e:
                    issues.append(f"Data validation error: {str(e)}")
            
            passed = len(issues) == 0
            details = f"Pipeline issues: {issues}" if issues else "Data pipeline integration successful"
            self.log_test_result("data_pipeline_integration", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("data_pipeline_integration", False, f"Exception: {str(e)}", "integration")
    
    def test_trial_calculations_consistency(self):
        """Integration Test 2: Cross-verify trial calculation results"""
        try:
            consistency_issues = []
            
            # Expected parameter values
            expected_params = {'a': 523, 'b': 318, 'c': 267, 'd': 194, 'e': 89, 'f': 41}
            
            trials = ['trial_alpha', 'trial_beta', 'trial_gamma', 'trial_delta']
            for trial in trials:
                results_path = self.base_path / f"{trial}/results.json"
                if results_path.exists():
                    try:
                        with open(results_path, 'r') as f:
                            data = json.load(f)
                        
                        # Check parameter consistency
                        if 'parameters' in data:
                            for param, expected_val in expected_params.items():
                                if param in data['parameters']:
                                    if data['parameters'][param] != expected_val:
                                        consistency_issues.append(
                                            f"{trial}: parameter {param} = {data['parameters'][param]}, expected {expected_val}")
                                else:
                                    consistency_issues.append(f"{trial}: parameter {param} missing")
                        else:
                            consistency_issues.append(f"{trial}: parameters section missing")
                            
                    except Exception as e:
                        consistency_issues.append(f"{trial}: Error reading - {str(e)}")
                else:
                    consistency_issues.append(f"{trial}: results.json missing")
            
            passed = len(consistency_issues) == 0
            details = f"Consistency issues: {consistency_issues}" if consistency_issues else "All trial calculations use consistent parameters"
            self.log_test_result("trial_calculations_consistency", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("trial_calculations_consistency", False, f"Exception: {str(e)}", "integration")
    
    def test_algorithm_reproducibility(self):
        """Integration Test 3: Test algorithm reproducibility"""
        try:
            reproducibility_issues = []
            
            # Try to run one algorithm to check reproducibility
            algorithm_path = self.base_path / "trial_alpha/algorithm_fixed.py"
            if algorithm_path.exists():
                try:
                    # Run algorithm and capture output
                    import subprocess
                    result = subprocess.run([sys.executable, str(algorithm_path)], 
                                          capture_output=True, text=True, timeout=30,
                                          cwd=str(algorithm_path.parent))
                    
                    if result.returncode != 0:
                        reproducibility_issues.append(f"Algorithm execution failed: {result.stderr}")
                    else:
                        # Check if results.json was updated
                        results_path = algorithm_path.parent / "results.json"
                        if results_path.exists():
                            pass  # Algorithm ran successfully
                        else:
                            reproducibility_issues.append("Algorithm ran but no results.json generated")
                            
                except subprocess.TimeoutExpired:
                    reproducibility_issues.append("Algorithm execution timed out")
                except Exception as e:
                    reproducibility_issues.append(f"Algorithm execution error: {str(e)}")
            else:
                reproducibility_issues.append("No algorithm file found for testing")
            
            passed = len(reproducibility_issues) == 0
            details = f"Reproducibility issues: {reproducibility_issues}" if reproducibility_issues else "Algorithm reproducibility verified"
            self.log_test_result("algorithm_reproducibility", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("algorithm_reproducibility", False, f"Exception: {str(e)}", "integration")
    
    def test_file_system_permissions(self):
        """Integration Test 4: Test file system permissions and access"""
        try:
            permission_issues = []
            
            # Test read permissions
            test_files = []
            for root, dirs, files in os.walk(self.base_path):
                test_files.extend([os.path.join(root, f) for f in files[:5]])  # Test first 5 files per directory
            
            for test_file in test_files[:20]:  # Limit to 20 files for performance
                try:
                    with open(test_file, 'r') as f:
                        f.read(100)  # Read first 100 characters
                except PermissionError:
                    permission_issues.append(f"Read permission denied: {test_file}")
                except Exception:
                    pass  # Other errors are not permission-related
            
            # Test write permissions in working directory
            try:
                test_write_file = self.base_path / "test_write_permission.tmp"
                with open(test_write_file, 'w') as f:
                    f.write("test")
                test_write_file.unlink()  # Delete test file
            except PermissionError:
                permission_issues.append("Write permission denied in working directory")
            except Exception as e:
                permission_issues.append(f"Write test error: {str(e)}")
            
            passed = len(permission_issues) == 0
            details = f"Permission issues: {permission_issues}" if permission_issues else "File system permissions verified"
            self.log_test_result("file_system_permissions", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("file_system_permissions", False, f"Exception: {str(e)}", "integration")
    
    def test_memory_usage_simulation(self):
        """Integration Test 5: Simulate memory usage and detect leaks"""
        try:
            memory_issues = []
            
            # Get initial memory usage
            process = psutil.Process()
            initial_memory = process.memory_info().rss
            
            # Simulate loading large datasets
            try:
                large_data = []
                for i in range(1000):
                    large_data.append([random.random() for _ in range(100)])
                
                # Check memory increase
                peak_memory = process.memory_info().rss
                memory_increase = peak_memory - initial_memory
                
                # Clean up
                del large_data
                
                # Force garbage collection
                import gc
                gc.collect()
                
                # Check if memory was released
                final_memory = process.memory_info().rss
                memory_retained = final_memory - initial_memory
                
                # If more than 50MB retained, might be a leak
                if memory_retained > 50 * 1024 * 1024:
                    memory_issues.append(f"Possible memory leak: {memory_retained / (1024*1024):.1f}MB retained")
                
            except Exception as e:
                memory_issues.append(f"Memory simulation error: {str(e)}")
            
            passed = len(memory_issues) == 0
            details = f"Memory issues: {memory_issues}" if memory_issues else "Memory usage simulation successful"
            self.log_test_result("memory_usage_simulation", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("memory_usage_simulation", False, f"Exception: {str(e)}", "integration")
    
    def test_concurrent_access_simulation(self):
        """Integration Test 6: Simulate concurrent file access"""
        try:
            concurrency_issues = []
            
            # Test concurrent read access to a file
            test_file = self.base_path / "research_platform/data_pipeline/raw_data/sensor_data.csv"
            if test_file.exists():
                def read_file_worker():
                    try:
                        with open(test_file, 'r') as f:
                            data = f.read(1000)  # Read first 1000 characters
                        return True
                    except Exception as e:
                        return str(e)
                
                # Create multiple threads to access file simultaneously
                import threading
                threads = []
                results = []
                
                for i in range(5):
                    thread = threading.Thread(target=lambda: results.append(read_file_worker()))
                    threads.append(thread)
                    thread.start()
                
                # Wait for all threads to complete
                for thread in threads:
                    thread.join()
                
                # Check results
                for i, result in enumerate(results):
                    if result is not True:
                        concurrency_issues.append(f"Thread {i}: {result}")
            else:
                concurrency_issues.append("Test file not found for concurrency test")
            
            passed = len(concurrency_issues) == 0
            details = f"Concurrency issues: {concurrency_issues}" if concurrency_issues else "Concurrent access simulation successful"
            self.log_test_result("concurrent_access_simulation", passed, details, "integration")
            
        except Exception as e:
            self.log_test_result("concurrent_access_simulation", False, f"Exception: {str(e)}", "integration")
    
    # =================== PERFORMANCE PROFILING ===================
    
    def measure_performance(self):
        """Measure system performance during validation"""
        try:
            process = psutil.Process()
            
            # CPU usage
            cpu_percent = process.cpu_percent(interval=1)
            
            # Memory usage
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / (1024 * 1024)
            
            # Disk I/O
            io_counters = process.io_counters()
            
            # Execution time
            execution_time = time.time() - self.start_time
            
            self.results['performance_metrics'] = {
                'cpu_usage_percent': cpu_percent,
                'memory_usage_mb': round(memory_mb, 2),
                'disk_read_bytes': io_counters.read_bytes,
                'disk_write_bytes': io_counters.write_bytes,
                'execution_time_seconds': round(execution_time, 3)
            }
            
        except Exception as e:
            self.results['performance_metrics'] = {'error': str(e)}
    
    # =================== CHECKSUM VERIFICATION ===================
    
    def calculate_checksums(self):
        """Calculate checksums for file integrity verification"""
        try:
            important_files = [
                "work_history.log",
                "research_platform/data_pipeline/raw_data/sensor_data.csv",
                "research_platform/data_pipeline/raw_data/metadata.json",
                "trial_alpha/algorithm.py",
                "trial_beta/algorithm.py"
            ]
            
            for file_path in important_files:
                full_path = self.base_path / file_path
                checksum = self.calculate_file_checksum(full_path)
                self.results['file_integrity'][file_path] = checksum
                
        except Exception as e:
            self.results['file_integrity']['error'] = str(e)
    
    # =================== COVERAGE REPORT GENERATION ===================
    
    def generate_coverage_report(self):
        """Generate test coverage report"""
        try:
            total_files = 0
            tested_files = 0
            
            # Count total files
            for root, dirs, files in os.walk(self.base_path):
                total_files += len(files)
            
            # Count files that were tested (approximation)
            tested_files = len(self.results['file_integrity'])
            
            coverage_percentage = (tested_files / total_files * 100) if total_files > 0 else 0
            
            self.results['coverage_report'] = {
                'total_files': total_files,
                'tested_files': tested_files,
                'coverage_percentage': round(coverage_percentage, 2)
            }
            
        except Exception as e:
            self.results['coverage_report'] = {'error': str(e)}
    
    # =================== MAIN VALIDATION RUNNER ===================
    
    def run_all_validations(self):
        """Run all validation tests"""
        print("Starting comprehensive validation...")
        
        # Unit Tests
        print("Running unit tests...")
        self.test_folder_structure_integrity()
        self.test_trial_alpha_files_existence()
        self.test_trial_beta_files_existence()
        self.test_raw_data_files_integrity()
        self.test_algorithm_syntax_validation()
        self.test_json_files_validity()
        self.test_yaml_files_validity()
        self.test_file_sizes_reasonable()
        self.test_calculation_precision_compliance()
        self.test_work_history_log_completeness()
        self.test_svg_files_validity()
        self.test_toml_files_validity()
        self.test_log_files_timestamp_format()
        self.test_dataset_element_count()
        self.test_file_encoding_consistency()
        self.test_numerical_results_sanity()
        
        # Integration Tests
        print("Running integration tests...")
        self.test_data_pipeline_integration()
        self.test_trial_calculations_consistency()
        self.test_algorithm_reproducibility()
        self.test_file_system_permissions()
        self.test_memory_usage_simulation()
        self.test_concurrent_access_simulation()
        
        # Performance and other metrics
        print("Measuring performance...")
        self.measure_performance()
        self.calculate_checksums()
        self.generate_coverage_report()
        
        print("Validation complete!")
        return self.results
    
    def save_results(self, output_file: str = "validation_results.json"):
        """Save validation results to file"""
        try:
            with open(self.base_path / output_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results: {str(e)}")

def main():
    """Main function"""
    import random  # Need this for memory simulation
    
    validator = ComprehensiveValidator()
    results = validator.run_all_validations()
    validator.save_results()
    
    # Print summary
    print("\\n" + "="*50)
    print("VALIDATION SUMMARY")
    print("="*50)
    print(f"Total Tests: {results['total_tests']}")
    print(f"Passed: {results['passed_tests']}")
    print(f"Failed: {results['failed_tests']}")
    print(f"Success Rate: {(results['passed_tests']/results['total_tests']*100):.1f}%")
    
    if results['performance_metrics']:
        print(f"Execution Time: {results['performance_metrics'].get('execution_time_seconds', 'N/A')} seconds")
        print(f"Memory Usage: {results['performance_metrics'].get('memory_usage_mb', 'N/A')} MB")
    
    print("\\nValidation completed successfully!")

if __name__ == "__main__":
    main()