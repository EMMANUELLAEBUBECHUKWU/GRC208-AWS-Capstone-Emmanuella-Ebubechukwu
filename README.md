# GRC208 AWS Integrated GRC Platform
## Capstone Project — Emmanuella Ebubechukwu

**Student:** Emmanuella Ebubechukwu  
**Student ID:** 2025/GRC/10041  
**Programme:** GRC Engineering (CGRCE)  
**Institution:** International Cybersecurity and Digital Forensics Academy (ICDFA)  
**Course:** GRC208 — Governance, Risk, and Compliance Capstone  
**Submission Date:** March 29, 2026  

---

## Overview

This repository contains the complete deployment of an AWS-native Governance, Risk, and Compliance (GRC) platform, built and submitted as the GRC208 capstone project. The platform was deployed from scratch in the AWS Academy Learner Lab environment using AWS CloudShell, Infrastructure as Code via CloudFormation, and a serverless Lambda-based compliance automation engine.

The project demonstrates how modern organisations can move beyond manual, spreadsheet-based compliance tracking and build a continuously monitored, automatically alerting GRC platform using AWS native services.

---

## Deployment Environment

| Detail | Value |
|--------|-------|
| AWS Account | 975049998247 |
| Region | us-east-1 |
| Deployment Method | AWS CloudShell via AWS Academy Learner Lab |
| Network | VPC vpc-013f73c5f62dd802b (10.0.0.0/16) |
| Database Endpoint | grc-capstone-db.cnok20k42m82.us-east-1.rds.amazonaws.com |
| Lambda Function | grc-compliance-monitor (Python 3.11, 256 MB) |
| CloudTrail Trail | grc-trail (IsLogging: True) |
| Test Results | 22/22 passing |

---

## Architecture Summary

The platform is built on a multi-tier VPC architecture with public and private subnets across two availability zones. All application compute and database resources are placed in private subnets with no direct internet exposure.

**Network Layer**
- VPC (10.0.0.0/16) with two public and two private subnets
- NAT Gateway for outbound-only private subnet internet access
- Application Load Balancer in public subnets
- Four security groups with scoped least-privilege rules

**Data Layer**
- Amazon RDS MySQL 8.0 (grc-capstone-db, db.t3.micro) — GRC relational data
- Amazon S3 — evidence storage and compliance reports
- Amazon DynamoDB — three tables for real-time compliance status
- AWS KMS — encryption at rest for RDS and S3

**Application Layer**
- AWS Lambda (grc-compliance-monitor) — hourly compliance automation
- Amazon ECS Fargate — containerised GRC dashboard application
- AWS EventBridge — hourly schedule triggering compliance Lambda

**Security & Compliance Layer**
- AWS Config — configured for 596 resource types, continuous recording
- AWS CloudTrail — grc-trail, all API calls logged to S3
- Amazon CloudWatch — alarm grc-high-non-compliance (<80% threshold)
- Amazon SNS — compliance threshold alert notifications

---

## Compliance Frameworks Supported

The platform supports mapping controls to the following six frameworks:

| Framework | Focus Area |
|-----------|------------|
| ISO 27001:2022 | Information Security Management System |
| NIST Cybersecurity Framework | Risk management and security controls |
| PCI DSS 3.2.1 | Payment card data protection |
| HIPAA | Health information privacy and security |
| GDPR | EU personal data protection |
| SOC 2 | Service organisation control assurance |

---

## Repository Structure



GRC208-AWS-Capstone-Emmanuella-Ebubechukwu/
├── README.md                              # This file
├── DEPLOYMENT_GUIDE.md                    # Step-by-step deployment walkthrough
├── BEST_PRACTICES.md                      # AWS and security best practices applied
├── AWS_SERVICES_GUIDE.md                  # Per-service documentation
├── architecture_design.md                 # System architecture and design decisions
├── PROJECT_MANIFEST.md                    # Complete file inventory
├── DELIVERY_SUMMARY.md                    # Capstone delivery evidence
├── cloudformation-network-stack.yaml      # Network infrastructure IaC
├── cloudformation-database-stack.yaml     # Database infrastructure IaC
├── lambda_compliance_monitor.py           # Compliance monitoring Lambda
├── grc-dashboard.jsx                      # React GRC dashboard
├── grc-dashboard.css                      # Dashboard styling
├── test_cases.py                          # 22-test validation suite
├── sample_data.sql                        # Database initialisation data
├── requirements.txt                       # Python dependencies
├── deploy.sh                              # Deployment automation script
├── architecture-diagram.md               # Architecture diagrams
├── .gitignore                             # Git configuration
└── screenshots/                           # 27 deployment evidence screenshots


---

## Quick Start

### Prerequisites
- AWS Academy Learner Lab access (or AWS account with appropriate permissions)
- AWS CloudShell (no local installation required)

### Deployment Steps

```bash
# 1. Clone this repository into CloudShell
git clone https://github.com/EMMANUELLAEBUBECHUKWU/GRC208-AWS-Capstone-Emmanuella-Ebubechukwu.git
cd GRC208-AWS-Capstone-Emmanuella-Ebubechukwu

# 2. Deploy network infrastructure
aws cloudformation create-stack \
  --stack-name grc-capstone-network-stack \
  --template-body file://cloudformation-network-stack.yaml \
  --parameters ParameterKey=EnvironmentName,ParameterValue=grc-capstone \
  --region us-east-1

# 3. Deploy database infrastructure
aws cloudformation create-stack \
  --stack-name grc-capstone-database-stack \
  --template-body file://cloudformation-database-stack.yaml \
  --parameters \
    ParameterKey=EnvironmentName,ParameterValue=grc-capstone \
    ParameterKey=DBUsername,ParameterValue=grcadmin \
    ParameterKey=DBPassword,ParameterValue=YourSecurePassword \
  --capabilities CAPABILITY_IAM \
  --region us-east-1


For the complete five-phase deployment walkthrough, see DEPLOYMENT_GUIDE.md.

Test Results
All 22 unit tests pass. Run the test suite with:

python3 test_cases.py




|Category             |Tests |Result    |
|---------------------|------|----------|
|Compliance Monitoring|3     |✓ Pass    |
|Risk Assessment      |3     |✓ Pass    |
|Data Validation      |4     |✓ Pass    |
|Database Operations  |3     |✓ Pass    |
|Compliance Frameworks|2     |✓ Pass    |
|Audit Logging        |3     |✓ Pass    |
|Report Generation    |2     |✓ Pass    |
|Integration Workflows|2     |✓ Pass    |
|**Total**            |**22**|**✓ 100%**|

Known Constraints
AWS Config Delivery Channel: The AWS Config delivery channel to S3 could not be activated in the AWS Academy Learner Lab environment. The Learner Lab LabRole does not have the S3 write permissions that AWS Config requires for delivery channel configuration. The configuration recorder (grc-config-recorder) exists and is set up for 596 resource types with continuous recording. This is a documented platform constraint specific to the Learner Lab IAM restrictions, not a configuration error.

Learning Outcomes
This capstone project demonstrates practical competency in:
	∙	Designing and deploying multi-tier cloud architectures on AWS
	∙	Writing Infrastructure as Code using AWS CloudFormation
	∙	Building serverless compliance automation with AWS Lambda
	∙	Implementing audit logging and monitoring with CloudTrail and CloudWatch
	∙	Mapping technical controls to GRC compliance frameworks
	∙	Deploying and managing managed database services on AWS

Author
Emmanuella EbubechukwuGRC Engineering (CGRCE) | ICDFAStudent ID: 2025/GRC/10041grc2510041@students.icdfa.edu.ng
Submitted: April, 2026


---
