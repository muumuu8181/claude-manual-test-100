#!/usr/bin/env python3
"""
Data Generator Script
Created by: テストAI7
Generates dummy data for CSV and JSON files with reproducible random seeds
"""

import csv
import json
import random
import numpy as np
from typing import List, Dict, Any
import time

class DataGenerator:
    """
    Data generation utility class
    """
    
    def __init__(self, seed: int = 42):
        """
        Initialize with random seed for reproducibility
        """
        self.seed = seed
        random.seed(seed)
        np.random.seed(seed)
    
    def generate_csv_data(self, rows: int, columns: List[str], filename: str):
        """
        Generate CSV data with specified structure
        """
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(columns)
            
            # Generate data rows
            for i in range(rows):
                row = []
                for col in columns:
                    if 'id' in col.lower():
                        row.append(i + 1)
                    elif 'feature' in col.lower():
                        row.append(round(random.uniform(0.1, 10.0), 3))
                    elif 'target' in col.lower():
                        row.append(round(random.uniform(1.0, 100.0), 2))
                    elif 'category' in col.lower():
                        row.append(random.choice(['A', 'B', 'C']))
                    elif 'name' in col.lower():
                        row.append(f"Item_{i+1}")
                    elif 'value' in col.lower():
                        row.append(round(random.uniform(0, 1000), 2))
                    elif 'date' in col.lower():
                        row.append(f"2025-01-{(i % 30) + 1:02d}")
                    else:
                        row.append(round(random.uniform(0, 100), 3))
                
                writer.writerow(row)
        
        print(f"Generated CSV: {filename} with {rows} rows")
    
    def generate_json_data(self, structure: Dict[str, Any], filename: str):
        """
        Generate structured JSON data
        """
        generated_data = {}
        
        for key, value in structure.items():
            if isinstance(value, dict):
                if 'type' in value:
                    if value['type'] == 'list':
                        size = value.get('size', 10)
                        item_type = value.get('item_type', 'random')
                        
                        if item_type == 'random':
                            generated_data[key] = [round(random.uniform(0, 100), 3) for _ in range(size)]
                        elif item_type == 'integer':
                            generated_data[key] = [random.randint(1, 1000) for _ in range(size)]
                        elif item_type == 'string':
                            generated_data[key] = [f"item_{i}" for i in range(size)]
                        elif item_type == 'object':
                            generated_data[key] = [
                                {
                                    'id': i + 1,
                                    'value': round(random.uniform(0, 100), 3),
                                    'label': f"Object_{i+1}"
                                } for i in range(size)
                            ]
                    
                    elif value['type'] == 'random':
                        min_val = value.get('min', 0)
                        max_val = value.get('max', 100)
                        precision = value.get('precision', 3)
                        generated_data[key] = round(random.uniform(min_val, max_val), precision)
                    
                    elif value['type'] == 'integer':
                        min_val = value.get('min', 1)
                        max_val = value.get('max', 100)
                        generated_data[key] = random.randint(min_val, max_val)
                    
                    elif value['type'] == 'choice':
                        choices = value.get('choices', ['A', 'B', 'C'])
                        generated_data[key] = random.choice(choices)
                    
                    elif value['type'] == 'nested':
                        generated_data[key] = self.generate_nested_object(value.get('structure', {}))
                
                else:
                    # Recursively generate nested dictionaries
                    generated_data[key] = self.generate_json_data(value, None)
            
            else:
                generated_data[key] = value
        
        if filename:
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(generated_data, jsonfile, indent=2, ensure_ascii=False)
            print(f"Generated JSON: {filename}")
        
        return generated_data
    
    def generate_nested_object(self, structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate nested object structure
        """
        result = {}
        for key, config in structure.items():
            if config['type'] == 'random':
                result[key] = round(random.uniform(config.get('min', 0), config.get('max', 100)), 3)
            elif config['type'] == 'integer':
                result[key] = random.randint(config.get('min', 1), config.get('max', 100))
            elif config['type'] == 'string':
                result[key] = f"{config.get('prefix', 'item')}_{random.randint(1, 1000)}"
        return result
    
    def generate_experiment_data(self, experiment_name: str):
        """
        Generate data specifically for experiment folders
        """
        # CSV input data
        csv_columns = ['iteration', 'parameter_a', 'parameter_b', 'expected_result', 'actual_result']
        self.generate_csv_data(20, csv_columns, f"{experiment_name}/input_data.csv")
        
        # JSON configuration
        config_structure = {
            "experiment_name": experiment_name,
            "parameters": {
                "learning_rate": {"type": "random", "min": 0.001, "max": 0.1, "precision": 4},
                "batch_size": {"type": "integer", "min": 16, "max": 128},
                "epochs": {"type": "integer", "min": 50, "max": 500}
            },
            "created_by": "テストAI7",
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S')
        }
        
        self.generate_json_data(config_structure, f"{experiment_name}/config.json")
        
        # Results JSON
        results_structure = {
            "final_accuracy": {"type": "random", "min": 0.7, "max": 0.99, "precision": 4},
            "training_loss": {"type": "list", "size": 10, "item_type": "random"},
            "validation_scores": {"type": "list", "size": 5, "item_type": "random"},
            "execution_time_ms": {"type": "random", "min": 100, "max": 5000, "precision": 2},
            "model_parameters": {
                "type": "nested",
                "structure": {
                    "weights_count": {"type": "integer", "min": 1000, "max": 10000},
                    "bias_count": {"type": "integer", "min": 10, "max": 100},
                    "memory_usage_mb": {"type": "random", "min": 50, "max": 500, "precision": 1}
                }
            }
        }
        
        self.generate_json_data(results_structure, f"{experiment_name}/output_results.json")
    
    def generate_test_cases(self, filename: str, num_cases: int = 20):
        """
        Generate test cases JSON
        """
        test_cases = []
        
        for i in range(num_cases):
            test_case = {
                "id": f"TEST_{i+1:03d}",
                "description": f"Test case {i+1} - Validation of component functionality",
                "input": {
                    "parameters": [round(random.uniform(0, 100), 3) for _ in range(3)],
                    "config": {
                        "mode": random.choice(["production", "development", "testing"]),
                        "verbose": random.choice([True, False])
                    }
                },
                "expected_output": {
                    "status": random.choice(["pass", "fail", "warning"]),
                    "value": round(random.uniform(0, 1000), 2),
                    "execution_time_ms": round(random.uniform(1, 100), 3)
                },
                "priority": random.choice(["high", "medium", "low"]),
                "category": random.choice(["unit", "integration", "performance", "regression"])
            }
            test_cases.append(test_case)
        
        test_structure = {
            "test_suite": "Comprehensive Validation Suite",
            "created_by": "テストAI7",
            "creation_date": time.strftime('%Y-%m-%d'),
            "total_test_cases": num_cases,
            "test_cases": test_cases
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(test_structure, f, indent=2, ensure_ascii=False)
        
        print(f"Generated test cases: {filename} with {num_cases} test cases")
    
    def generate_all_missing_data(self):
        """
        Generate all missing data files for the project
        """
        print("Generating missing data files...")
        
        # Generate datasets if missing
        try:
            datasets_path = "research_project/datasets/"
            
            # Training data
            if not os.path.exists(f"{datasets_path}training_data.csv"):
                training_columns = ['id', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'target', 'category']
                self.generate_csv_data(100, training_columns, f"{datasets_path}training_data.csv")
            
            # Test data
            if not os.path.exists(f"{datasets_path}test_data.csv"):
                test_columns = ['id', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'target', 'category']
                self.generate_csv_data(30, test_columns, f"{datasets_path}test_data.csv")
            
        except Exception as e:
            print(f"Note: Dataset generation skipped - {e}")
        
        # Generate test cases
        try:
            self.generate_test_cases("validation_suite/test_cases.json", 25)
        except Exception as e:
            print(f"Note: Test cases generation skipped - {e}")
        
        print("Data generation completed!")

def main():
    """
    Main function to demonstrate data generation capabilities
    """
    print("Data Generator Script - Created by テストAI7")
    print("=" * 50)
    
    generator = DataGenerator(seed=12345)
    
    # Demo: Generate sample CSV
    print("\nGenerating sample CSV...")
    sample_csv_columns = ['id', 'name', 'value', 'category', 'date']
    generator.generate_csv_data(15, sample_csv_columns, "sample_data.csv")
    
    # Demo: Generate sample JSON
    print("\nGenerating sample JSON...")
    sample_json_structure = {
        "metadata": {
            "version": "1.0",
            "created_by": "テストAI7"
        },
        "data": {
            "type": "list",
            "size": 5,
            "item_type": "object"
        },
        "statistics": {
            "mean_value": {"type": "random", "min": 50, "max": 150, "precision": 2},
            "max_value": {"type": "random", "min": 200, "max": 300, "precision": 2},
            "sample_count": {"type": "integer", "min": 100, "max": 1000}
        }
    }
    
    generator.generate_json_data(sample_json_structure, "sample_data.json")
    
    # Demo: Generate test cases
    print("\nGenerating test cases...")
    generator.generate_test_cases("sample_test_cases.json", 10)
    
    print("\nData generation demonstration completed!")
    print("Generated files: sample_data.csv, sample_data.json, sample_test_cases.json")

if __name__ == "__main__":
    import os
    main()