# **Postmortem: SurveyForm Web Application Outage — Lessons Learned and Road to Resilience**

### ***Incident Report for SurveyForm Web Application Outage***

#### ***Incident Summary:***

On June 22, 2024, the SurveyForm web application experienced a significant outage that lasted approximately 4 hours from 10:00 AM to 2:00 PM UTC. During this period, users were unable to access the survey forms, submit responses, or manage their surveys via the application interface.

#### ***Timeline of Events:***

10:00 AM UTC: Monitoring systems detected a sudden increase in error rates and latency on the SurveyForm application.
10:05 AM UTC: Initial investigation began by the operations team to identify the root cause of the issue.
10:20 AM UTC: It was determined that the application’s backend API was intermittently returning 500 Internal Server Errors.
10:30 AM UTC: Engineering teams were alerted and joined the investigation to diagnose the issue further.
11:00 AM UTC: Database queries and logs were analyzed, revealing that a recent deployment of a survey form management feature coincided with the onset of errors.
11:30 AM UTC: A rollback of the recent deployment was initiated as a precautionary measure to restore service stability.
12:00 PM UTC: Despite the rollback, errors persisted intermittently, indicating a more complex underlying issue.
1:00 PM UTC: Deep dive into database performance metrics revealed that a database connection pool configuration change inadvertently reduced the maximum connections allowed, leading to connection timeouts and subsequent application errors.
1:30 PM UTC: Immediate adjustments were made to restore the original database connection pool configuration.
2:00 PM UTC: After confirming stable performance metrics and conducting thorough testing, the SurveyForm application was fully restored to normal operation.

#### ***Root Cause:***

The root cause of the outage was traced to a recent change in the database connection pool configuration. Specifically, a deployment included an unintended reduction in the maximum allowed connections, causing database connection timeouts under moderate to heavy load conditions. This configuration change was not adequately tested in a production-like environment prior to deployment, leading to its unforeseen impact during peak usage hours.

#### ***Mitigation and Resolution:***

To address the outage and prevent recurrence, the following actions were taken:

**Immediate rollback:** Reverted the recent deployment to mitigate immediate errors.
**Database connection pool adjustment:** Restored the original configuration settings to accommodate expected load and prevent connection timeouts.
**Testing and validation:** Implemented stricter testing protocols for database configuration changes, including thorough load testing in staging environments.
**Monitoring enhancements:** Enhanced monitoring and alerting systems to quickly detect and respond to similar issues in the future.

#### ***Conclusion:***

The SurveyForm outage on June 22, 2024, was a challenging experience that highlighted the importance of robust testing and careful configuration management in maintaining application stability. By implementing the outlined mitigation strategies and follow-up actions, we aim to strengthen our systems and processes to prevent similar incidents in the future.
