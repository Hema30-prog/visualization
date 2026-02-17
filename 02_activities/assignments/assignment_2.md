# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
I used the Helpdesk dashboard - https://public.tableau.com/app/profile/andreea.scintei/viz/HelpDeskRWFD_17334321633050/1_Summary as a good data visualization.

Aesthetic Strengths

The dashboard has a clean, professional layout with a well-organized grid structure. KPI cards are aligned consistently across the top, creating balance and symmetry. The use of a limited color palette (navy, grey, and pink) maintains visual cohesion without overwhelming the viewer. Color is applied purposefully to indicate performance direction (e.g., downward arrows in pink/red for declines, blue for improvement). Typography is clear and hierarchical—large bold numbers emphasize key metrics, while supporting details such as prior month comparisons are smaller but readable. 

Perceptual Strengths

The dashboard follows strong visual hierarchy principles. The most important metrics (Total, Resolved, Open, Avg Days Open, Backlog) are positioned at the top for immediate visibility. Bar charts are used effectively for categorical comparisons (severity, issue type, owner group), allowing accurate comparison through length. 

Substantive Strengths

Substantively, the dashboard provides meaningful operational insights. It addresses workload volume, resolution rates, backlog levels, satisfaction distribution, severity, and ownership allocation. Including percentage changes and prior month comparisons adds context beyond static reporting. Multiple breakdowns allow diagnostic analysis and support informed decision-making. 


How could this data visualization have been improved?

1. Aesthetic Improvements

• Improve Color Consistency
Pink is used for multiple meanings (negative change, Unknown satisfaction, Hardware, Unassigned severity). Assign one clear meaning per color to avoid confusion.

• Strengthen Visual Emphasis
Critical metrics such as 72% open tickets or 55.7% backlog could be more visually prominent through conditional formatting or subtle highlighting.

2. Perceptual Improvements

• Replace Donut Charts with Bar Charts
Bar charts allow more accurate comparison than donut charts because humans judge length better than angles.

• Sort All Bars Descending
Ensure severity, issue type, and owner group charts are clearly ranked to speed up interpretation.


3️. Substantive Improvements

• Add Targets or SLA Benchmarks
Without targets, it’s unclear whether performance is acceptable.



I used superstore https://public.tableau.com/app/profile/stanke/viz/KPIDesigns/KPIDesign as bad data visualization

Aesthetic Weaknesses

The dashboard lacks visual structure and design cohesion. Large empty spaces create imbalance, while the metrics are loosely arranged without clear grouping or alignment. The repeated display of the same information (Sales vs. Monthly Revenue, Profit vs. Monthly Profit, etc.) creates redundancy and makes the layout feel cluttered rather than streamlined. Color usage is minimal and inconsistent—red and blue arrows indicate change, but there is no cohesive visual theme or hierarchy guiding the viewer’s attention. The design is text-heavy and resembles a spreadsheet rather than a thoughtfully designed analytical dashboard. There are no visual anchors, charts, or graphical elements to add engagement or balance.

Perceptual Weaknesses

Perceptually, the dashboard is weak because it relies almost entirely on numbers and text. Humans process visual patterns (length, position, shape) more effectively than raw figures, yet no bar charts, line charts, or comparative visuals are included. There is no trend visualization, no ranking, and no proportional comparison. The repeated presentation of metrics increases cognitive load and may confuse viewers about which values are primary. Additionally, there is no strong visual emphasis on the dramatic decline in profit (-69%), which should stand out as critical.

Substantive Weaknesses

Substantively, the dashboard provides limited analytical insight. It reports key performance indicators but does not explain why changes occurred. There are no breakdowns by region, category, or time trend, and no performance benchmarks or targets. The data is descriptive rather than diagnostic, limiting its usefulness for decision-making or strategic action.


How could this data visualization have been improved?


Aesthetic Improvements (Design & Layout)

• Remove Redundancy
The same metrics (Sales, Profit, Margin, Orders) are repeated multiple times. Keep one clean KPI row and eliminate duplicate “Monthly” sections to reduce clutter.


• Strengthen Color Strategy
Use a consistent and meaningful color system:

Red = decline

Green = growth

Neutral colors for labels
Avoid mixing blue and red inconsistently.

Perceptual Improvements (Clarity & Comparison)

• Add Trend Visualizations
Include sparklines or small line charts to show 6–12 month trends for sales and profit. Trends are easier to interpret than static values.

• Add Comparative Visuals
Use:

Bar charts for year-over-year comparison

Bullet charts for actual vs. target

Humans interpret length and position more accurately than text.

Substantive Improvements (Insight & Analysis)

• Add Context and Benchmarks
Include targets or industry benchmarks to indicate whether performance is acceptable.

• Provide Breakdown Analysis
Add segmentation by:

Region

Product category

Customer segment

This explains why profit dropped.

      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 02/16/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
