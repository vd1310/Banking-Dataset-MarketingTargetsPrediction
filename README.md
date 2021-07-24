# Data Analytics Boot Camp Final Project

## Presentation

### Topic

Every business has a limited marketing budget. Therefore it's vital that each dollar is spent in the most efficient way possible. In a bank's case, it's necessary to determine which of their clients will be receptive to phone marketing campaigns regarding the bank's financial services, specifically term deposits. Term deposits are similar to GICs, where a client will give the bank money in exchange for the money plus interest after a fixed period of time. During this time, the client is unable to withdraw their money.

### Motivation

The motivation behind the topic is to determine if marketing campaigns through phone calls is an effective use of marketing spend by companies such as a bank or large institution. This could also shed light on why so many people recieve fraudulent phone calls of people claiming to be from IRS/CRA demanding money. If phone campaigns are truly effective, then one would expect to continue receiving fraudulent calls.

### Data Background

The data was pulled from the [UCI Machine learning repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing). The data was gathered from marketing campaigns a Portuguese banking institution implemented through phone calls.

Source: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014

### Questions to Answer

Primary Goal:
- To determine whether or not a bank client would be interested in a term deposit subscription based on their profile and past history with the bank. This will enable the bank to better target their phone based marketing efforts towards clients who would be open to a term deposit subscription.

Secondary Goal(s)
- Determine if there is an upper limit on the amount of marketing campaigns a client can receive before terminating communication
- Determine if a relationship between a client's profile and their usage of financial services exists

## Machine Learning

The purpose of our machine learning is to analyse the data and identify patterns based on which we could make predictions on new data. Here the marketing data (referred to above) was split into two; train(45,211) and test(4,521) randomly selected points. 
- SMOTE algorithm is used to fit the model. This reduces the risk of oversampling by increasing the minority class.
- GradientBoostingClassifier boosting method is used to progressively reduce errors to the barest minimum

## Communication Protocols

Group communication will be located on a Slack group that each member will join. Any updates or changes throughout the project will be posted in this group chat. Additionally members will be able to direct message any other member of the group in order to ask them questions or make comments about the project, the data or the work. Microsoft Teams and WhatsApp are used to communicate between members.

## Github Branch System

Each member of the group will maintain their own branch to do their work in. Members can create new branches to outline specific work they are doing. For example, a branch name could be "Andrew_Tam_seg1_model" to illustrate Andrew is working on the branch which contains the work for the machine learning model and is intended for segment 1.
ww
## Technology

See the *technology.md* file in the repo.
