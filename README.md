\# Retail Market Intelligence Platform



An automated retail research and analytics platform designed to evaluate product opportunities, calculate estimated profitability, and support data-driven business decisions.



\*\*Project Status:\*\* Phase 1 completed — Local Python development and Continuous Integration (CI).



\## Project Overview



This project demonstrates the development of a retail intelligence application using Python, software engineering best practices, and cloud-native technologies.



The long-term objective is to create an AWS-based platform capable of collecting product research data, analyzing customer feedback, evaluating competitors, and generating automated research reports.



The application currently runs locally using synthetic product data.



\## Phase 1 — Python Development and CI/CD



\*\*Status: Completed\*\*



\### 1. Repository Setup



\- Created a local Git repository using Git Bash.

\- Established the `main` branch.

\- Organized the project into dedicated directories for application code, data, tests, documentation, and infrastructure.

\- Published the repository to GitHub.



\### 2. Python Development Environment



\- Installed and verified Python 3.15.2.

\- Created and activated a virtual environment using `venv`.

\- Verified pip was available within the environment.

\- Configured `.gitignore` to exclude virtual environments and sensitive files.



\### 3. Product Research Engine



Developed a Python application that:



\- Reads synthetic product records from JSON.

\- Extracts selling prices and estimated costs.

\- Calculates estimated contribution profit per unit.

\- Calculates estimated contribution margins.

\- Estimates monthly contribution using hypothetical sales volumes.

\- Ranks products by estimated monthly contribution.

\- Generates a report in the terminal.



\*\*Key files:\*\*



\- `src/research.py` — Loads data and generates reports.

\- `src/scoring.py` — Calculates financial metrics and validates inputs.

\- `data/sample\_products.json` — Contains synthetic product data.



\### 4. Input Validation



Added validation to detect:



\- Missing required product fields.

\- Zero or negative selling prices.

\- Negative cost values.

\- Invalid numeric types.



Invalid inputs raise descriptive `ValueError` exceptions.



\### 5. Automated Unit Testing



Implemented tests using Python's built-in `unittest` framework.



The current tests verify:



\- Correct profitability calculations.

\- Rejection of zero-price products.



\*\*Results:\*\* 2 tests passed.



\### 6. Continuous Integration — GitHub Actions



Configured GitHub Actions to automatically execute Python unit tests when code is pushed to `main` or a pull request targets `main`.



\*\*CI environment:\*\*



\- GitHub-hosted Ubuntu runner.

\- Python 3.13.

\- Python `unittest`.



\*\*Result:\*\* First GitHub Actions workflow completed successfully.



\## Current Architecture



```text

Synthetic Product Data (JSON)

&#x20;            |

&#x20;            v

&#x20;   Python Research Engine

&#x20;            |

&#x20;            v

&#x20;Profitability Calculations

&#x20;            |

&#x20;            v

&#x20;      Product Ranking

&#x20;            |

&#x20;            v

&#x20;    Terminal Research Report

```



GitHub Actions independently executes automated unit tests against the Python application.



\## Technology Stack



\*\*Implemented:\*\*

\- Python

\- JSON

\- Git and GitHub

\- Python unittest

\- GitHub Actions

\- Python virtual environments



\*\*Planned:\*\*

\- AWS Lambda

\- Amazon S3

\- Amazon DynamoDB

\- Amazon EventBridge

\- AWS Step Functions

\- Terraform

\- Amazon Bedrock

\- MCP integrations



\## Running the Application



Clone the repository and navigate into the project directory.



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it on Windows using Git Bash:



```bash

source .venv/Scripts/activate

```



Run the application:



```bash

python src/research.py

```



Run the automated tests:



```bash

python -m unittest discover -s tests -v

```



The application currently uses fictional data for development and testing. Its results are not real Amazon sales forecasts or fully burdened profit estimates.



\## Phase 2 — AWS Cloud Deployment



\*\*Status: Planned\*\*



Next development objectives:



1\. Prepare the research engine for AWS Lambda execution.

2\. Create an S3 bucket for research data and reports.

3\. Configure IAM permissions using least privilege.

4\. Deploy and test the application in AWS.

5\. Configure logging and monitoring using Amazon CloudWatch.

6\. Introduce scheduled automation using EventBridge.



\## Future Development



\- Integrate authorized external product research APIs and MCP services.

\- Automate competitor and customer sentiment analysis.

\- Develop AI-assisted product opportunity scoring.

\- Build an automated research dashboard.

\- Implement infrastructure as code using Terraform.

\- Monitor pipeline reliability, processing costs, and data quality.



\## Engineering Skills Demonstrated



\- Python programming and modular application design.

\- Data ingestion and processing.

\- Input validation and error handling.

\- Automated unit testing.

\- Git version control.

\- Continuous Integration using GitHub Actions.

\- Software documentation and reproducible workflows.



\## Disclaimer



All current product records, sales estimates, and financial outputs are synthetic and intended for software development and testing purposes.

