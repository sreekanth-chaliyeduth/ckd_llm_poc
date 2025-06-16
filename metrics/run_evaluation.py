#!/usr/bin/env python3
from eval_driver import LLMEvaluator
from test_matrix import get_test_matrix
import pandas as pd
import json
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_html_report(results_df: pd.DataFrame, summary: dict):
    """Generate HTML report with interactive charts"""
    # Create subplot figure
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Prediction Accuracy Distribution",
            "Explanation Quality Distribution",
            "Response Time Analysis",
            "Risk Factors Accuracy"
        )
    )

    # Add prediction accuracy histogram
    fig.add_trace(
        go.Histogram(x=results_df["prediction_accuracy"], name="Prediction Accuracy"),
        row=1, col=1
    )

    # Add explanation quality histogram
    fig.add_trace(
        go.Histogram(x=results_df["explanation_quality"], name="Explanation Quality"),
        row=1, col=2
    )

    # Add response time box plot
    fig.add_trace(
        go.Box(y=results_df["response_time"], name="Response Time"),
        row=2, col=1
    )

    # Add risk factors accuracy bar chart
    fig.add_trace(
        go.Bar(
            x=results_df["test_case_id"],
            y=results_df["risk_factors_accuracy"],
            name="Risk Factors Accuracy"
        ),
        row=2, col=2
    )

    # Update layout
    fig.update_layout(
        height=800,
        width=1200,
        title_text="LLM Evaluation Results",
        showlegend=False
    )

    # Save as HTML
    fig.write_html(os.path.join("reports", "llm_evaluation_report.html"))

def main():
    # Initialize evaluator
    evaluator = LLMEvaluator(use_dummy=True)
    
    # Get test matrix
    test_cases = get_test_matrix()
    
    # Run evaluation
    print("Running LLM evaluation matrix...")
    results_df = evaluator.run_evaluation_matrix(test_cases)
    
    # Calculate summary
    summary = {
        "mean_prediction_accuracy": results_df["prediction_accuracy"].mean(),
        "mean_confidence_score": results_df["confidence_score"].mean(),
        "mean_explanation_quality": results_df["explanation_quality"].mean(),
        "mean_response_time": results_df["response_time"].mean(),
        "mean_risk_factors_accuracy": results_df["risk_factors_accuracy"].mean(),
        "total_test_cases": len(results_df)
    }
    
    # Generate HTML report
    generate_html_report(results_df, summary)
    
    # Print summary
    print("\nEvaluation Summary:")
    print("==================")
    print(f"Total test cases: {len(results_df)}")
    print(f"Mean prediction accuracy: {results_df['prediction_accuracy'].mean():.2f}")
    print(f"Mean explanation quality: {results_df['explanation_quality'].mean():.2f}")
    print(f"Mean response time: {results_df['response_time'].mean():.2f} seconds")
    print(f"Mean risk factors accuracy: {results_df['risk_factors_accuracy'].mean():.2f}")
    
    # Print detailed results
    print("\nDetailed Results:")
    print("================")
    for _, row in results_df.iterrows():
        print(f"\nTest Case: {row['test_case_id']}")
        print(f"Prediction Accuracy: {row['prediction_accuracy']:.2f}")
        print(f"Explanation Quality: {row['explanation_quality']:.2f}")
        print(f"Response Time: {row['response_time']:.2f}s")
        print(f"Risk Factors Accuracy: {row['risk_factors_accuracy']:.2f}")
    
    print("\nResults saved in reports/ directory:")
    print("- llm_evaluation.csv")
    print("- llm_evaluation_summary.json")
    print("- llm_classification_report.json")
    print("- llm_evaluation_report.html")

if __name__ == "__main__":
    main() 