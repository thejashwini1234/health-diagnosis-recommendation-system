from flask import Blueprint, render_template, request
import pandas as pd

symptom_checker = Blueprint('symptom_checker', __name__, template_folder="templates")

# Load dataset
df = pd.read_csv("health.csv")

# Collect all symptoms
symptoms = sorted(set(df["symptom1"]).union(df["symptom2"]).union(df["symptom3"]))
symptoms.insert(0, "none")  # allow blank choice

@symptom_checker.route("/", methods=["GET", "POST"])
def checker():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        s1 = request.form.get("symptom1")
        s2 = request.form.get("symptom2")
        s3 = request.form.get("symptom3")

        selected_symptoms = [s1, s2, s3]

        results = []
        selected_set = {s for s in selected_symptoms if s != "none"}
 
        for _, row in df.iterrows():
            row_set = {row["symptom1"], row["symptom2"], row["symptom3"]}
            
            # flexible check: if selected symptoms are a subset of disease symptoms
            if selected_set.issubset(row_set):
                results.append({
                    "disease": row["disease"],
                    "remedies": str(row["remedies"]).split(";")
                })

        # ✅ Limit to 2 results only
        results = results[:2]

        return render_template(
            "diagnosis_result.html", 
            name=name, age=age, 
            results=results, 
            selected_symptoms=selected_symptoms,
            symptoms=symptoms
        )

    return render_template("symptom_checker.html", symptoms=symptoms)
