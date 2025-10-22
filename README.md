# E-commerce Test Automation Suite

## 🚀 Project Overview

A comprehensive test automation framework for e-commerce web applications, built using Selenium WebDriver with Python. This project demonstrates practical skills in automated testing, including test design, execution, and maintenance.

**Current Status:** 🔨 Active Development | Core test scripts completed, framework implementation in progress

---

## 📋 Project Objectives

- Automate end-to-end testing workflows for e-commerce platforms
- Implement industry-standard design patterns for maintainable test code
- Develop reusable test components and utilities
- Generate comprehensive test execution reports
- Demonstrate professional test automation practices

---

## ✅ Completed Features

### Test Coverage
- **User Authentication:** Login validation with valid/invalid credentials
- **Shopping Cart:** Add/remove items, cart quantity verification
- **Checkout Flow:** Complete purchase workflow from cart to order confirmation
- **Product Interactions:** Search, filtering, product detail validation
- **Dropdown Handling:** Sorting and selection automation

### Technical Implementation
- Element identification using multiple locator strategies (ID, XPath, CSS Selectors, Class Names)
- Explicit and implicit wait mechanisms for stable test execution
- Chrome browser configuration with customized options (incognito mode, notification handling)
- Error handling and exception management
- Git version control with structured commit history

---

## 🔄 In Progress

### Framework Development
- **PyTest Integration:** Migrating test scripts to PyTest framework for better organization
  - Test fixtures for setup/teardown
  - Parameterized testing capabilities
  - HTML report generation
  
- **Page Object Model (POM):** Refactoring code to separate page logic from test logic
  - Creating page classes for LoginPage, ProductPage, CartPage, CheckoutPage
  - Implementing reusable page methods
  - Improving code maintainability and scalability

- **Test Data Management:** Externalizing test data for data-driven testing

- **Enhanced Reporting:** Implementing detailed test execution reports with screenshots

---

## 🛠️ Technologies & Tools

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.x |
| **Automation** | Selenium WebDriver |
| **Test Framework** | PyTest (in progress) |
| **Browser** | Chrome/ChromeDriver |
| **Version Control** | Git, GitHub |
| **Design Pattern** | Page Object Model (implementing) |

---

## 📁 Project Structure

```
e-commerce-test-automation/
├── day1-tests/              # Initial test scripts
│   ├── test_setup.py
│   ├── test_google_search.py
│   ├── test_login.py
│   └── practice_locators.py
│
├── day2-tests/              # Advanced test scenarios
│   ├── test_implicit_wait.py
│   ├── test_explicit_wait.py
│   ├── test_add_to_cart.py
│   ├── test_dropdown.py
│   └── test_complete_checkout.py
│
├── tests/                   # PyTest-organized tests (in development)
├── pages/                   # Page Object Model classes (in development)
├── utils/                   # Helper functions and utilities
├── test_data/              # Test data files
├── reports/                # Test execution reports
├── screenshots/            # Test failure screenshots
├── requirements.txt        # Python dependencies
├── learning-log.md         # Development progress tracking
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/selenium-learning-journey.git
   cd selenium-learning-journey
   ```

2. **Install dependencies**
   ```bash
   pip install selenium
   pip install pytest
   pip install pytest-html
   ```

3. **Configure ChromeDriver**
   - Download ChromeDriver from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
   - Extract and place in a known location (e.g., `C:/chromedriver/`)
   - Update the path in test files if needed

---

## 🚀 Running Tests

### Current Test Execution

**Run individual test files:**
```bash
# Basic tests
python day1-tests/test_login.py

# Advanced scenarios
python day2-tests/test_add_to_cart.py
python day2-tests/test_complete_checkout.py
```

### PyTest Execution (Coming Soon)

```bash
# Run all tests
pytest tests/

# Run with HTML report
pytest tests/ --html=reports/test_report.html

# Run specific test file
pytest tests/test_checkout.py

# Run with verbose output
pytest tests/ -v
```

---

## 🎯 Test Scenarios Covered

### 1. User Authentication
- Valid login credentials
- Invalid username/password handling
- Login form validation

### 2. Shopping Cart Management
- Adding single product to cart
- Adding multiple products
- Cart count verification
- Viewing cart contents

### 3. Product Browsing
- Dropdown sorting (price, name)
- Product selection
- Navigation between pages

### 4. Checkout Process
- Cart to checkout flow
- Form filling (shipping information)
- Order review
- Order confirmation verification

---

## 📚 Key Learnings & Skills Demonstrated

### Selenium WebDriver Expertise
- Multiple element locator strategies
- Synchronization techniques (waits)
- Browser options configuration
- Handling dynamic web elements

### Test Design Principles
- Separation of concerns
- Reusable test components
- Clear test structure
- Descriptive naming conventions

### Problem-Solving
- Debugging failing tests
- Handling browser-specific popups
- Managing element visibility issues
- Error handling and recovery

---

## 🔮 Roadmap & Next Steps

### Short-term (Next 1-2 Weeks)
- [ ] Complete PyTest migration for all test scripts
- [ ] Implement Page Object Model for all pages
- [ ] Add pytest fixtures for browser setup/teardown
- [ ] Generate comprehensive HTML test reports
- [ ] Implement screenshot capture on test failures

### Medium-term
- [ ] Add data-driven testing with external data sources
- [ ] Implement parallel test execution
- [ ] Add API testing integration
- [ ] Create CI/CD pipeline with GitHub Actions
- [ ] Expand test coverage to additional workflows

### Long-term
- [ ] Multi-browser support (Firefox, Edge)
- [ ] Performance testing integration
- [ ] Database validation tests
- [ ] Comprehensive test documentation

---

## 📖 Documentation

- **[Learning Log](learning-log.md):** Daily progress and lessons learned
- **Test Case Documentation:** Coming soon
- **Architecture Guide:** Coming soon

---

## 🤝 About This Project

This project is part of my journey to develop professional test automation skills. It represents hands-on learning with industry-standard tools and practices. The project is continuously evolving as I learn new concepts and implement best practices.

### Current Focus
- Strengthening Selenium WebDriver fundamentals
- Learning PyTest framework thoroughly
- Implementing Page Object Model pattern
- Building maintainable and scalable test architecture

---

## 📧 Contact

**Anjor Patil**
- Email: anjorpatil16@gmail.com
- LinkedIn: www.linkedin.com/in/anjor-patil-29207a213
- Location: Kolhapur, Maharashtra, India

---

## 📝 License

This is a personal learning project created for educational and portfolio purposes.

---

**Last Updated:** October 2025  
**Status:** Active Development - Building practical test automation skills through hands-on implementation
