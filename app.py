import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

# import dash_core_components as dcc
# import dash_html_components as html

# Read the data from CSV
data = pd.read_csv("train.csv")
styles = {
    "credits": {
        "font-size": "16px",
        "color": "#555555",
        "margin-top": "20px",
        "padding": "10px",
        "background-color": "#f7f7f7",
        "border": "1px solid #dddddd",
        "border-radius": "5px",
    }
}
# Survival rate based on gender
gender_survival_count = (
    data.groupby(["Survived", "Sex"]).size().reset_index(name="Count")
)
fig_bar = px.bar(
    gender_survival_count,
    x="Sex",
    y="Count",
    color="Survived",
    barmode="group",
    labels={"Sex": "Gender", "Count": "Count", "Survived": "Survival"},
)
fig_bar.update_layout(title_text="Count of Survivors vs. Non-Survivors by Gender")

# Proportion of survivors and non-survivors by passenger class
class_survival_count = (
    data.groupby(["Survived", "Pclass"]).size().reset_index(name="Count")
)
fig_pie = px.pie(
    class_survival_count,
    values="Count",
    names="Pclass",
    color="Survived",
    labels={"Count": "Count", "Pclass": "Passenger Class", "Survived": "Survival"},
    title="Proportion of Survivors and Non-Survivors by Passenger Class",
)

# Age vs. Fare with Survival Status
fig_scatter = px.scatter(
    data, x="Age", y="Fare", color="Survived", title="Age vs. Fare with Survival Status"
)

# Distribution of fares for survivors and non-survivors by passenger class
fig_box = px.box(
    data,
    x="Pclass",
    y="Fare",
    color="Survived",
    labels={"Pclass": "Passenger Class", "Fare": "Fare", "Survived": "Survival"},
    title="Distribution of Fares for Survivors and Non-Survivors by Passenger Class",
)


# Hypothesis 1: Survival rate based on passenger class and gender
class_gender_survival_count = (
    data.groupby(["Survived", "Pclass", "Sex"]).size().reset_index(name="Count")
)
fig_bar_h1 = px.bar(
    class_gender_survival_count,
    x="Pclass",
    y="Count",
    color="Survived",
    barmode="group",
    facet_col="Sex",
    facet_row="Survived",
    labels={
        "Pclass": "Passenger Class",
        "Count": "Count",
        "Survived": "Survival",
        "Sex": "Gender",
    },
    title="Count of Survivors vs. Non-Survivors by Passenger Class and Gender",
)

# Hypothesis 2: Age distribution of survivors and non-survivors
fig_box_h2 = px.box(
    data,
    x="Survived",
    y="Age",
    color="Survived",
    labels={"Survived": "Survival", "Age": "Age"},
    title="Distribution of Ages for Survivors and Non-Survivors",
)

# Hypothesis 3: Fare distribution based on passenger class and survival status
fig_violin_h3 = px.violin(
    data,
    x="Pclass",
    y="Fare",
    color="Survived",
    labels={"Pclass": "Passenger Class", "Fare": "Fare", "Survived": "Survival"},
    title="Distribution of Fares by Passenger Class and Survival",
)

# Hypothesis 4: Survival rate based on port of embarkation
embarked_survival_count = (
    data.groupby(["Survived", "Embarked"]).size().reset_index(name="Count")
)
fig_bar_h4 = px.bar(
    embarked_survival_count,
    x="Embarked",
    y="Count",
    color="Survived",
    barmode="group",
    labels={
        "Embarked": "Port of Embarkation",
        "Count": "Count",
        "Survived": "Survival",
    },
    title="Count of Survivors vs. Non-Survivors by Port of Embarkation",
)

# Hypothesis 5: Survival rate based on the number of family members onboard
family_survival_count = (
    data.groupby(["Survived", "SibSp"]).size().reset_index(name="Count")
)
fig_bar_h5 = px.bar(
    family_survival_count,
    x="SibSp",
    y="Count",
    color="Survived",
    barmode="group",
    labels={
        "SibSp": "Number of Siblings/Spouses",
        "Count": "Count",
        "Survived": "Survival",
    },
    title="Count of Survivors vs. Non-Survivors by Number of Siblings/Spouses",
)
# Hypothesis 6: Survival rate based on the fare paid
fig_box_h6 = px.box(
    data,
    x="Survived",
    y="Fare",
    color="Survived",
    labels={"Survived": "Survival", "Fare": "Fare"},
    title="Distribution of Fares for Survivors and Non-Survivors",
)

# Hypothesis 7: Survival rate based on the number of parents/children onboard
fig_bar_h7 = px.bar(
    data.groupby(["Survived", "Parch"]).size().reset_index(name="Count"),
    x="Parch",
    y="Count",
    color="Survived",
    barmode="group",
    labels={
        "Parch": "Number of Parents/Children",
        "Count": "Count",
        "Survived": "Survival",
    },
    title="Count of Survivors vs. Non-Survivors by Number of Parents/Children",
)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(
    [
        html.H1("Titanic Dataset Analysis", style={"text-align": "center"}),
        html.H2("Survival Rate based on Gender"),
        dcc.Graph(figure=fig_bar),
        html.H2("Proportion of Survivors and Non-Survivors by Passenger Class"),
        dcc.Graph(figure=fig_pie),
        html.H2("Age vs. Fare with Survival Status"),
        dcc.Graph(figure=fig_scatter),
        html.H2(
            "Distribution of Fares for Survivors and Non-Survivors by Passenger Class"
        ),
        dcc.Graph(figure=fig_box),
        html.H2("Hypothesis 1: Survival Rate based on Passenger Class and Gender"),
        html.H3(
            "Bar Chart: Show the count of survivors vs. non-survivors based on passenger class and gender."
        ),
        dcc.Graph(figure=fig_bar_h1),
        html.P(
            "Explanation of Hypothesis 1: This bar chart displays the count of survivors vs. non-survivors based on passenger class and gender, with separate bars for each combination of gender and survival status."
        ),
        html.H2("Hypothesis 2: Age Distribution of Survivors and Non-Survivors"),
        html.H3(
            "Box Plot: Compare the distribution of ages for survivors and non-survivors."
        ),
        dcc.Graph(figure=fig_box_h2),
        html.P(
            "Explanation of Hypothesis 2: This box plot compares the age distributions for survivors and non-survivors, displaying the median, quartiles, and any outliers for each group."
        ),
        html.H2(
            "Hypothesis 3: Fare Distribution based on Passenger Class and Survival Status"
        ),
        html.H3(
            "Violin Plot: Visualize the distribution of fares based on passenger class and survival status."
        ),
        dcc.Graph(figure=fig_violin_h3),
        html.P(
            "Explanation of Hypothesis 3: This violin plot shows the distribution of fares based on passenger class and survival status. It provides insights into the fare ranges and density for each combination."
        ),
        html.H2("Hypothesis 4: Survival Rate based on Port of Embarkation"),
        html.H3(
            "Bar Chart: Show the count of survivors vs. non-survivors based on port of embarkation."
        ),
        dcc.Graph(figure=fig_bar_h4),
        html.P(
            "Explanation of Hypothesis 4: This bar chart displays the count of survivors vs. non-survivors based on the port of embarkation. It provides insights into whether the port of embarkation had an impact on survival rates."
        ),
        html.H2("Hypothesis 5: Survival Rate based on Number of Siblings/Spouses"),
        html.H3(
            "Bar Chart: Show the count of survivors vs. non-survivors based on the number of siblings/spouses."
        ),
        dcc.Graph(figure=fig_bar_h5),
        html.P(
            "Explanation of Hypothesis 5: This bar chart displays the count of survivors vs. non-survivors based on the number of siblings/spouses onboard. It helps analyze the relationship between family size and survival rates."
        ),
        html.H2("Hypothesis 6: Survival Rate based on Fare Paid"),
        html.H3(
            "Box Plot: Compare the distribution of fares for survivors and non-survivors."
        ),
        dcc.Graph(figure=fig_box_h6),
        html.P(
            "Explanation of Hypothesis 6: This box plot compares the fare distributions for survivors and non-survivors. It helps analyze whether the fare paid had an impact on survival rates."
        ),
        html.H2("Hypothesis 7: Survival Rate based on Number of Parents/Children"),
        html.H3(
            "Bar Chart: Show the count of survivors vs. non-survivors based on the number of parents/children."
        ),
        dcc.Graph(figure=fig_bar_h7),
        html.P(
            "Explanation of Hypothesis 7: This bar chart displays the count of survivors vs. non-survivors based on the number of parents/children onboard. It helps analyze the relationship between family size and survival rates."
        ),
        html.Div(
            [
                html.H2("Conclusions"),
                html.P(
                    "Based on the correlation heatmap, you can draw the following conclusions:"
                ),
                html.Ul(
                    [
                        html.Li(
                            "Fare and Pclass: There is a strong negative correlation between fare and passenger class (Pclass). This indicates that higher passenger class (lower class number) is associated with higher fares."
                        ),
                        html.Li(
                            "Age and Pclass: There is a weak negative correlation between age and passenger class (Pclass). This suggests that higher passenger class tends to be associated with slightly younger passengers."
                        ),
                        html.Li(
                            "Survived and Pclass: There is a moderate negative correlation between survival and passenger class (Pclass). This implies that passengers in higher classes had a higher chance of survival."
                        ),
                        html.Li(
                            "Survived and Fare: There is a weak positive correlation between survival and fare. It suggests that passengers who paid higher fares had a slightly higher chance of survival."
                        ),
                    ]
                ),
            ]
        ),
        # Adding the description using html.P()
        html.Div(
            [
                html.H2("Credits", style={"margin-bottom": "10px"}),
                html.P(
                    "Used Plotly to create these visualizations."
                    "Plotly is an open-source data visualization library that provides a wide range of interactive plotting capabilities. "
                    "It allows users to create visually appealing and interactive graphs, charts, and dashboards in Python, R, and JavaScript. "
                    "It is a data visualization library that offers a rich set of tools for creating interactive plots and charts. "
                    "It provides support for various programming languages, including Python, R, and JavaScript, making it versatile and widely used in data science, analytics, and business intelligence applications. "
                    "It supports a wide range of plot types, including scatter plots, bar charts, and 3D plots. "
                    "Plotly also provides data exploration tools and can be used to build interactive dashboards and web applications."
                ),
            ],
            style=styles["credits"],
        ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
