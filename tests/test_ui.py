import pytest
from playwright.sync_api import Page, expect
import time

def test_home_page(page: Page):
    """Test the home page loads correctly"""
    # Wait for server to be ready
    time.sleep(2)
    page.goto("/")
    
    # Check page title
    expect(page).to_have_title("CKD Prediction System")
    
    # Check main heading
    heading = page.get_by_role("heading", name="Chronic Kidney Disease Prediction")
    expect(heading).to_be_attached()

def test_prediction_form(page: Page):
    """Test the prediction form submission"""
    # Wait for server to be ready
    time.sleep(2)
    page.goto("/")
    
    # Fill form
    page.get_by_label("Age:").fill("65")
    page.get_by_label("Blood Pressure:").fill("140")
    page.get_by_label("Red Blood Cells:").select_option("normal")
    page.get_by_label("Blood Glucose Random:").fill("117")
    page.get_by_label("Blood Urea:").fill("56")
    page.get_by_label("Serum Creatinine:").fill("3.8")
    
    # Submit form
    page.get_by_role("button", name="Predict").click()
    
    # Check result
    result = page.get_by_text("Prediction Result")
    expect(result).to_be_attached()

def test_form_validation(page: Page):
    """Test form validation"""
    # Wait for server to be ready
    time.sleep(2)
    page.goto("/")
    
    # Try to submit empty form
    page.get_by_role("button", name="Predict").click()
    
    # Check validation messages
    error = page.locator("#errorMessage")
    expect(error).to_be_attached()

def test_responsive_design(page: Page):
    """Test responsive design"""
    # Wait for server to be ready
    time.sleep(2)
    
    # Test mobile view
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    
    # Check mobile layout
    form = page.locator("form#predictionForm")
    expect(form).to_be_attached()
    
    # Test tablet view
    page.set_viewport_size({"width": 768, "height": 1024})
    page.goto("/")
    
    # Check tablet layout
    expect(form).to_be_attached()
    
    # Test desktop view
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    
    # Check desktop layout
    expect(form).to_be_attached() 