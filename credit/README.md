**Requirements for the Policy Maker Agent**

---

### **Overview**
The Policy Maker Agent (PMA) is a sophisticated AI-driven system designed to assist organizations in creating, managing, and pricing credit policies. It incorporates data-driven decision-making tools, compliance mechanisms, and dynamic pricing strategies to enable optimal policy formulation across the credit lifecycle. The PMA will operate in various stages, from acquisition to collections, and provide actionable insights and final policies tailored to borrower segments and investor requirements.

---

### **1. Objectives**
1. **End-to-End Policy Formulation**:
   - Create detailed credit policies under predefined classes (e.g., prime, near-prime, subprime borrowers).
   - Provide optimized pricing strategies aligned with risk and market conditions.

2. **Dynamic Pricing**:
   - Incorporate real-time market data, borrower risk scores, and profitability models to determine interest rates and fees for credit products.

3. **Regulatory Compliance**:
   - Ensure all policies comply with relevant laws and regulations (e.g., lending limits, usury laws).

4. **Investor-Focused Analytics**:
   - Offer reports that evaluate portfolio performance metrics such as yield, default rates, and net interest margins.

---

### **2. Functional Requirements**

#### **2.1. Credit Policy Formulation**
- **Class Creation**:
  - Define borrower categories (e.g., prime, near-prime, subprime) based on creditworthiness metrics such as FICO scores and income stability.
- **Policy Terms**:
  - Set terms and conditions for each class, including:
    - Maximum loan amounts.
    - Repayment schedules (e.g., monthly installments, balloon payments).
    - Collateral requirements.
- **Customizable Parameters**:
  - Allow users to input custom thresholds (e.g., minimum credit scores) for policy customization.

#### **2.2. Risk Assessment Tools**
- **Credit Risk Analysis**:
  - Evaluate borrower risk using factors such as:
    - Probability of Default (PD).
    - Loss Given Default (LGD).
    - Exposure at Default (EAD).
- **Risk-Based Pricing**:
  - Generate interest rates and fees based on risk profiles.

#### **2.3. Dynamic Pricing Engine**
- **Market Analysis**:
  - Monitor and integrate market trends (e.g., benchmark interest rates, competitor offerings).
- **Interest Rate Optimization**:
  - Adjust rates dynamically based on:
    - Borrower risk classification.
    - Portfolio diversification goals.
    - Cost of funds.
- **Fee Structures**:
  - Calculate origination fees, late payment penalties, and other administrative costs.

#### **2.4. Collections Management**
- **Delinquency Monitoring**:
  - Classify delinquent accounts into aging buckets (e.g., 30, 60, 90+ days past due).
- **Recovery Strategies**:
  - Recommend collection tactics, such as:
    - Payment restructuring options.
    - Referral to collection agencies.
- **Portfolio Health Metrics**:
  - Provide insights on recovery rates, write-offs, and legal proceedings.

#### **2.5. Investor Reporting**
- **Key Metrics**:
  - Offer detailed reports covering:
    - Net interest margin (NIM).
    - Yield.
    - Default and delinquency rates.
    - Risk-adjusted return metrics.
- **Scenario Analysis**:
  - Simulate portfolio performance under various economic conditions.
- **Custom Dashboards**:
  - Allow users to create dashboards with preferred metrics and visualizations.

#### **2.6. Compliance Management**
- **Regulatory Database Integration**:
  - Integrate with legal and regulatory databases for:
    - Lending limit checks.
    - Usury compliance.
    - Fair lending practices.
- **Automated Audits**:
  - Perform periodic audits to ensure compliance.

#### **2.7. SQLite Dataset Integration**
- **Available Datasets**:
  - Borrower Profiles: Detailed borrower information, including demographics and financial history.
  - Loan Products: Specifications and terms for various credit products.
  - Default Rates: Historical data on default probabilities segmented by borrower class.
  - Market Trends: Real-time data on interest rates, economic indicators, and competitor analysis.
  - Regulatory Data: Comprehensive information on lending regulations and compliance requirements.
- **Database Operations**:
  - Support for querying, updating, and appending data to these datasets.
  - Seamless integration for data-driven decision-making across all modules.

---

### **3. Non-Functional Requirements**

#### **3.1. Performance**
- **Response Time**:
  - The system should respond to user queries and generate reports within 5 seconds.
- **Scalability**:
  - Handle simultaneous processing for up to 100 users without performance degradation.

#### **3.2. Security**
- **Data Encryption**:
  - Ensure all sensitive data (e.g., borrower information) is encrypted at rest and in transit.
- **Access Control**:
  - Implement role-based access controls to restrict sensitive functionalities.

#### **3.3. Reliability**
- **Uptime**:
  - Ensure 99.9% system uptime.
- **Error Handling**:
  - Provide descriptive error messages and fallback mechanisms for failures.

#### **3.4. Usability**
- **Intuitive Interface**:
  - Offer a user-friendly interface with clear navigation.
- **Documentation**:
  - Provide comprehensive user manuals and FAQs.

---

### **4. Technical Requirements**

#### **4.1. Technology Stack**
- **Backend**: Python with LangChain framework.
- **Frontend**: React.js or Vue.js.
- **Database**: PostgreSQL for structured data and MongoDB for unstructured data.
- **AI/ML Models**:
  - Integrate with OpenAI or similar LLMs for natural language understanding.
  - Use predictive models for risk scoring.

#### **4.2. APIs and Integrations**
- **Third-Party APIs**:
  - Credit bureau data (e.g., Experian, TransUnion).
  - Regulatory compliance checks (e.g., AML/KYC providers).
- **Internal APIs**:
  - Connect with CRM and ERP systems.

#### **4.3. Deployment**
- **Cloud Infrastructure**: Deploy on AWS or Azure for scalability.
- **CI/CD Pipeline**: Automate testing and deployment.

---

### **5. User Stories**

#### **5.1. Policy Maker**
- As a policy maker, I want to create credit policies based on borrower classes so that I can address diverse customer needs.
- As a policy maker, I want to analyze delinquency data so that I can adjust collection strategies effectively.

#### **5.2. Risk Analyst**
- As a risk analyst, I want to assess credit risk using borrower data so that I can ensure sound underwriting decisions.
- As a risk analyst, I want to simulate portfolio performance under different scenarios so that I can prepare for economic changes.

#### **5.3. Investor**
- As an investor, I want to review portfolio yield and risk-adjusted returns so that I can evaluate my investments.
- As an investor, I want to access compliance reports so that I can ensure adherence to regulations.

#### **5.4. IT Administrator**
- As an IT administrator, I want to manage user roles and permissions so that sensitive functionalities are protected.
- As an IT administrator, I want to monitor system performance so that I can ensure reliability.

---

### **6. Future Enhancements**

#### **6.1. Advanced Risk Models**
- Incorporate machine learning models to improve PD, LGD, and EAD predictions.

#### **6.2. Global Compliance**
- Expand compliance management to cover international regulations.

#### **6.3. Real-Time Analytics**
- Enable real-time updates for portfolio metrics and risk assessments.

#### **6.4. Mobile Access**
- Develop a mobile application for on-the-go access to key functionalities.

---

### **7. Success Metrics**

1. **Policy Accuracy**: Policies created align with organizational goals and legal standards.
2. **Turnaround Time**: Reduction in time to generate policies and reports.
3. **User Satisfaction**: Achieve a 95% satisfaction score in user surveys.
4. **Portfolio Performance**: Improve yield while maintaining or lowering default rates.

---

### **Conclusion**
The Policy Maker Agent aims to revolutionize credit policy management by combining cutting-edge AI, dynamic pricing, and robust compliance tools. By addressing the outlined requirements, the system will enable organizations to create profitable and compliant policies while ensuring exceptional stakeholder satisfaction.



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
prompt_template = f"""
The user has asked the following question:
"{input_query}"

The following metrics have been suggested for analysis:
{', '.join(map(str, elicited_metrics)) if elicited_metrics else "None"}

The following metrics have been analyzed so far:
{', '.join(map(str, analyzed_metrics)) if analyzed_metrics else "None"}

Available data for analysis:
{available_data_str}

### Instructions:
1. Determine if the analyzed metrics are sufficient to provide a complete answer to the user's question.
2. If the analyzed metrics are insufficient, specify additional metrics to analyze, strictly based on the available data: {available_data_str}.
3. Provide details on any required calculations, including:
   - **Tables and Columns**: Specify the exact table names and columns needed.
   - **Joins**: Mention any necessary table joins and their keys.
   - **Formulas**: Provide calculation formulas using columns and tables.

### Output Format:
Respond with one of the following:
1. **Sufficient**: If the analyzed metrics fully answer the user's question.
2. **Additional Metrics Needed**: If additional metrics are required, provide the following in a clear format:
"""


llm_response = llm.invoke(prompt_template).content
print(llm_response)