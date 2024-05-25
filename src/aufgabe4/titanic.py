import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# AUFGABE 2
# a) Lesen Sie die Trainingsdaten ein und teilen Sie sie in ein Validierungsdatenset (20%) und in ein eigentliches
# Trainigsdatenset (80%) auf. Finden Sie auf dem Trainigsdatenset eine Regel für das Überleben alleine aufgrund der
# Klasse des Tickets (Pclass). Wenden Sie diese Regel auf die Validierungsdaten an. Wie gut ist die Genauigkeit (Anteil
# der korrekten Klassifikationen) auf den Validierungsdaten?

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Laden der Trainingsdaten
train_val = pd.read_csv('data/train.csv')

# Aufteilen in Trainings- (80%) und Validierungsdatensatz (20%)
train_data, val_data = train_test_split(train_val, test_size=0.2, random_state=42)

# Regel basierend auf Ticketklasse
def rule_based_on_pclass(df):
    # Annahme: Höhere Klasse hat höhere Überlebenswahrscheinlichkeit
    df['Survived_Pclass'] = df['Pclass'].apply(lambda x: 1 if x == 1 else 0)
    return df

train_data = rule_based_on_pclass(train_data)
val_data = rule_based_on_pclass(val_data)

# Genauigkeit auf Validierungsdatensatz
accuracy = accuracy_score(val_data['Survived'], val_data['Survived_Pclass'])
print(f'Genauigkeit basierend auf Pclass: {accuracy:.4f}')

# b) Wenden Sie die Regel aus a) auf die Testdaten an und laden Sie Ihre Lösung hoch.
# Laden der Testdaten
test_data = pd.read_csv('data/test.csv')

# Anwenden der Regel
test_data = rule_based_on_pclass(test_data)

# Erstellen der Ausgabedatei
pred_survived = test_data['Survived_Pclass']
output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': pred_survived})
output.to_csv('data/my_submission.csv', index=False)
print("Your submission was successfully saved!")

# c) Logistische Regression mit Pclass
# Trainieren Sie eine logistische Regression mit den Variablen 'Pclass'. Verwenden Sie die Klasse
# sklearn.linear_model.LogisticRegression. Berechnen Sie die Accuracy auf dem Validierungsset.

# Logistische Regression trainieren
logreg = LogisticRegression()
logreg.fit(train_data[['Pclass']], train_data['Survived'])

# Vorhersagen und Genauigkeit berechnen
val_preds = logreg.predict(val_data[['Pclass']])
accuracy_logreg = accuracy_score(val_data['Survived'], val_preds)
print(f'Genauigkeit der logistischen Regression basierend auf Pclass: {accuracy_logreg:.4f}')

# d.i) Missing Values:
# Verwenden Sie nun weitere Features. Die Variable Age enthält Missing values, die Sie durch folgenden code ersetzen
# können (was passiert da?)
val_data['Age'] = val_data['Age'].fillna(train_data['Age'].median(skipna=True))
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median(skipna=True))
# -> die Daten werden mit mittelwerten gefüllt

# d.ii) Kategorische Variable
# Verwenden Sie die Funktion pd.get_dummies um die Variablen 'Pclass' and 'Sex' in numerische Werte umzuwandeln. Führen
# Sie nun eine logistische Regression durch.
# Umwandeln von 'Pclass' und 'Sex' in numerische Werte
train_data = pd.get_dummies(train_data, columns=['Pclass', 'Sex'], drop_first=True)
val_data = pd.get_dummies(val_data, columns=['Pclass', 'Sex'], drop_first=True)
# -> aus einem kategorischen Wert werden mehrere binäre Werte. Also aus PCklass 1, 2, 3 werden 2 Spalten mit 0 und 1
# -> aus dem Geschlecht wird eine Spalte Sex_male mit 0 und 1, 0 impliziert weiblich, 1 impliziert männlich

# Logistische Regression trainieren
logreg = LogisticRegression()
logreg.fit(train_data[['Pclass_2', 'Pclass_3', 'Sex_male']], train_data['Survived'])

# Vorhersagen und Genauigkeit berechnen
val_preds = logreg.predict(val_data[['Pclass_2', 'Pclass_3', 'Sex_male']])
accuracy_logreg = accuracy_score(val_data['Survived'], val_preds)
print(f'Genauigkeit der logistischen Regression mit Pclass und Sex: {accuracy_logreg:.4f}')

# e) Weitere Klassifikatoren. Neben der logistischen Regression, gibt es weitere Klassifikatoren. Der Random-Forest ist
# ein recht stabiler Klassifikator, was wäre die Performance von diesem Klassifikator.

# Random Forest trainieren
rf = RandomForestClassifier()
rf.fit(train_data[['Pclass_2', 'Pclass_3', 'Sex_male']], train_data['Survived'])

# Vorhersagen und Genauigkeit berechnen
val_preds = rf.predict(val_data[['Pclass_2', 'Pclass_3', 'Sex_male']])
accuracy_rf = accuracy_score(val_data['Survived'], val_preds)
print(f'Genauigkeit des Random Forest Klassifikators: {accuracy_rf:.4f}')
