def valider(enregistrement):
    """
    Vérifie si un enregistrement est valide.
    Renvoie (True, "") si valide, sinon (False, "raison : ...")
    """
    try:
        nom, matiere, note, groupe = enregistrement
    except ValueError:
        return False, "raison : enregistrement mal formé (doit contenir 4 éléments)"
    
    if not isinstance(nom, str) or not nom.strip():
        return False, "raison : nom vide ou invalide"
    
    if not isinstance(matiere, str) or not matiere.strip():
        return False, "raison : matière vide ou invalide"
        
    if not isinstance(groupe, str) or not groupe.strip():
        return False, "raison : groupe vide ou invalide"
        
    try:
        note_float = float(note)
    except (ValueError, TypeError):
        return False, "raison : note non numérique"
        
    if not (0 <= note_float <= 20):
        return False, "raison : note hors intervalle [0, 20]"
        
    return True, ""


donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"),
 ("Bouchra", "Info", "abc", "G2"),
 ("", "Math", 10, "G1"),
 ("Yassine", "Info", 22, "G2"),
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"),
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Hana", "Physique", 15, "G3"),
 ("Hana", "Math", 8, "G3"),
]


print("="*50)
print(" PARTIE 1 : Nettoyage et validation")
print("="*50)

valides = []
erreurs = []
doublons_exact = set()
vus = set()

for ligne in donnees:
    # Détection des doublons exacts
    if ligne in vus:
        doublons_exact.add(ligne)
        continue  # On ignore le doublon pour la suite du traitement
    
    vus.add(ligne)
    
    # Validation
    est_valide, raison = valider(ligne)
    if est_valide:
        nom, matiere, note, groupe = ligne
        # On stocke les données propres (note convertie en float)
        valides.append((nom, matiere, float(note), groupe))
    else:
        erreurs.append({"ligne": ligne, "raison": raison})

print(f"Nombre de lignes valides   : {len(valides)}")
print(f"Nombre de lignes d'erreurs : {len(erreurs)}")
for err in erreurs:
    print(f"  -> {err}")
print(f"Nombre de doublons exacts  : {len(doublons_exact)} {doublons_exact}")
print("\n")


print("="*50)
print(" PARTIE 2 : Structuration")
print("="*50)

# 2.1 Matières distinctes (utilisation d'un set pour éviter les doublons)
matieres_distinctes = set()
for nom, matiere, note, groupe in valides:
    matieres_distinctes.add(matiere)

print(f"Matières enseignées distinctes : {matieres_distinctes}")

# 2.2 Hiérarchie (étudiant -> matière -> notes)
notes_par_etudiant = {}

# 2.3 Groupes pédagogiques (groupe -> set d'étudiants)
groupes_pedagogiques = {}

for nom, matiere, note, groupe in valides:
    # Remplissage hiérarchie étudiant
    if nom not in notes_par_etudiant:
        notes_par_etudiant[nom] = {}
    if matiere not in notes_par_etudiant[nom]:
        notes_par_etudiant[nom][matiere] = []
    
    notes_par_etudiant[nom][matiere].append(note)
    
    # Remplissage groupes pédagogiques
    if groupe not in groupes_pedagogiques:
        groupes_pedagogiques[groupe] = set()
    groupes_pedagogiques[groupe].add(nom)

print("\nNotes par étudiant (hiérarchie) :")
for etu, matieres in notes_par_etudiant.items():
    print(f"  {etu} : {matieres}")

print("\nÉtudiants par groupes pédagogiques :")
for grp, etudiants in groupes_pedagogiques.items():
    print(f"  {grp} : {etudiants}")
print("\n")


print("="*50)
print(" PARTIE 3 : Calculs et statistiques")
print("="*50)

def somme_recursive(liste_nombres):
    """
    Calcule la somme des éléments d'une liste de manière récursive.
    """
    if not liste_nombres:
        return 0
    return liste_nombres[0] + somme_recursive(liste_nombres[1:])

def calculer_moyenne(liste_nombres):
    """
    Calcule la moyenne en utilisant la fonction_somme_recursive.
    """
    if not liste_nombres:
        return 0
    return somme_recursive(liste_nombres) / len(liste_nombres)

moyennes_etudiants = {}

for etudiant, matieres in notes_par_etudiant.items():
    toutes_les_notes_etudiant = []
    moyennes_par_matiere = {}
    
    for matiere, notes in matieres.items():
        toutes_les_notes_etudiant.extend(notes)
        moyennes_par_matiere[matiere] = calculer_moyenne(notes)
    
    moyenne_generale = calculer_moyenne(toutes_les_notes_etudiant)
    moyennes_etudiants[etudiant] = {
        "generale": moyenne_generale,
        "par_matiere": moyennes_par_matiere
    }

print("Moyennes par étudiant :")
for etudiant, moy in moyennes_etudiants.items():
    print(f"  {etudiant} - Générale: {moy['generale']:.2f} | Par matière: {moy['par_matiere']}")
print("\n")


print("="*50)
print(" PARTIE 4 : Analyse avancée et détection d'anomalies")
print("="*50)

# Structure dédiée aux alertes
alertes = {
    "multiples_notes_meme_matiere": [],
    "profil_incomplet": [],
    "groupe_moyenne_faible": [],
    "ecarts_importants": []
}

# Seuils pour les anomalies
SEUIL_MOYENNE_FAIBLE = 10.0
SEUIL_ECART = 5.0 # Peut être adapté

# 1. Multiples notes pour une même matière (parcours par étudiant et matière)
for etudiant, matieres in notes_par_etudiant.items():
    for matiere, notes in matieres.items():
        if len(notes) > 1:
            alertes["multiples_notes_meme_matiere"].append((etudiant, matiere, notes))

# 2. Profil incomplet (des notes manquent comparé à l'ensemble global des matières distinctes)
for etudiant, matieres in notes_par_etudiant.items():
    # Si le nombre de matières de l'étudiant est inférieur au total de matières possibles
    if len(matieres) < len(matieres_distinctes):
        matieres_manquantes = matieres_distinctes - set(matieres.keys())
        alertes["profil_incomplet"].append((etudiant, matieres_manquantes))

# 3. Groupes pédagogiques présentant une moyenne générale faible
for groupe, etudiants in groupes_pedagogiques.items():
    notes_groupe = []
    for etudiant in etudiants:
        for matiere, notes in notes_par_etudiant[etudiant].items():
            notes_groupe.extend(notes)
            
    if notes_groupe:
        moyenne_groupe = calculer_moyenne(notes_groupe)
        if moyenne_groupe < SEUIL_MOYENNE_FAIBLE:
            alertes["groupe_moyenne_faible"].append({
                "groupe": groupe, 
                "moyenne": moyenne_groupe
            })

# 4. Écarts très importants entre notes min et max pour un étudiant
for etudiant, matieres in notes_par_etudiant.items():
    toutes_les_notes_etudiant = []
    for notes in matieres.values():
        toutes_les_notes_etudiant.extend(notes)
        
    if toutes_les_notes_etudiant:
        note_min = min(toutes_les_notes_etudiant)
        note_max = max(toutes_les_notes_etudiant)
        ecart = note_max - note_min
        if ecart >= SEUIL_ECART:
            alertes["ecarts_importants"].append({
                "etudiant": etudiant, 
                "min": note_min, 
                "max": note_max, 
                "ecart": ecart
            })

# Affichage des alertes de manière structurée
for type_alerte, liste_alertes in alertes.items():
    print(f"[{type_alerte.upper()}] ({len(liste_alertes)} alertes):")
    if not liste_alertes:
        print("  -> Aucune alerte.")
    else:
        for alerte in liste_alertes:
            print(f"  -> {alerte}")
    print()
