# Generated by Django 4.2.2 on 2023-06-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("NO", models.IntegerField(blank=True, null=True)),
                ("SAMPLE_ID", models.IntegerField(blank=True, null=True)),
                ("Food_Code", models.IntegerField(blank=True, null=True)),
                ("DB_Group", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "Commercial_Product",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("Food_Name", models.CharField(blank=True, max_length=100, null=True)),
                ("Year", models.IntegerField(blank=True, null=True)),
                (
                    "Manufacturer_Distributor",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "Food_Major_Category",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "Food_Subcategory",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("Single_Serving_Size", models.FloatField(blank=True, null=True)),
                (
                    "Content_Unit",
                    models.CharField(
                        blank=True,
                        choices=[("g", "g"), ("ml", "ml")],
                        max_length=2,
                        null=True,
                    ),
                ),
                ("Total_Content_g", models.FloatField(blank=True, null=True)),
                ("Total_Content_mL", models.FloatField(blank=True, null=True)),
                ("Energy_kcal", models.FloatField(blank=True, null=True)),
                ("Water_g", models.FloatField(blank=True, null=True)),
                ("Protein_g", models.FloatField(blank=True, null=True)),
                ("Fat_g", models.FloatField(blank=True, null=True)),
                ("Carbohydrates_g", models.FloatField(blank=True, null=True)),
                ("Total_Sugars_g", models.FloatField(blank=True, null=True)),
                ("Glucose_g", models.FloatField(blank=True, null=True)),
                ("Fructose_g", models.FloatField(blank=True, null=True)),
                ("Sugar_Alcohol_g", models.FloatField(blank=True, null=True)),
                ("Erythritol_g", models.FloatField(blank=True, null=True)),
                ("Total_Dietary_Fiber_g", models.FloatField(blank=True, null=True)),
                ("Calcium_mg", models.FloatField(blank=True, null=True)),
                ("Iron_mg", models.FloatField(blank=True, null=True)),
                ("Magnesium_mg", models.FloatField(blank=True, null=True)),
                ("Phosphorus_mg", models.FloatField(blank=True, null=True)),
                ("Potassium_mg", models.FloatField(blank=True, null=True)),
                ("Sodium_mg", models.FloatField(blank=True, null=True)),
                ("Zinc_mg", models.FloatField(blank=True, null=True)),
                ("Copper_mg", models.FloatField(blank=True, null=True)),
                ("Copper_mcq", models.FloatField(blank=True, null=True)),
                ("Manganese_mg", models.FloatField(blank=True, null=True)),
                ("Manganese_mcq", models.FloatField(blank=True, null=True)),
                ("Selenium_mcq", models.FloatField(blank=True, null=True)),
                ("Iodine_mcq", models.FloatField(blank=True, null=True)),
                ("Chloride_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_A_mcq_RE", models.FloatField(blank=True, null=True)),
                ("Beta_carotene_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_D_D2_D3_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_D3_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_D1_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_E_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_E_mg_alpha_TE", models.FloatField(blank=True, null=True)),
                ("Vitamin_K_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_K_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_K1_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_K2_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_B1_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_B1_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_B2_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_B2_mcq", models.FloatField(blank=True, null=True)),
                ("Niacin_mg_NE", models.FloatField(blank=True, null=True)),
                ("Pantothenic_Acid_mg", models.FloatField(blank=True, null=True)),
                ("Pantothenic_Acid_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_B6_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_B6_mcq", models.FloatField(blank=True, null=True)),
                ("Biotin_mcq", models.FloatField(blank=True, null=True)),
                ("Folate_DFE_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_B12_mg", models.FloatField(blank=True, null=True)),
                ("Vitamin_B12_mcq", models.FloatField(blank=True, null=True)),
                ("Vitamin_C_g", models.FloatField(blank=True, null=True)),
                ("Vitamin_C_mg", models.FloatField(blank=True, null=True)),
                ("Choline_mg", models.FloatField(blank=True, null=True)),
                ("Lysine_mg", models.FloatField(blank=True, null=True)),
                ("Tryptophan_mg", models.FloatField(blank=True, null=True)),
                ("Histidine_mg", models.FloatField(blank=True, null=True)),
                ("Arginine_mg", models.FloatField(blank=True, null=True)),
                ("Cysteine_mg", models.FloatField(blank=True, null=True)),
                ("Proline_mg", models.FloatField(blank=True, null=True)),
                ("Taurine_mg", models.FloatField(blank=True, null=True)),
                ("Cholesterol_g", models.FloatField(blank=True, null=True)),
                ("Cholesterol_mg", models.FloatField(blank=True, null=True)),
                (
                    "Total_Saturated_Fatty_Acids_g",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Linoleic_Acid_18_2_n_6_c_g",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Alpha_linolenic_Acid_18_3_n_3_mg",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Gamma_linolenic_Acid_18_3_n_6_mg",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Arachidonic_Acid_20_4_n_6_mg",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Eicosapentaenoic_Acid_20_5_n_3_mg",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "Docosahexaenoic_Acid_22_6_n_3_mg",
                    models.FloatField(blank=True, null=True),
                ),
                ("Sum_of_EPA_and_DHA_mg", models.FloatField(blank=True, null=True)),
                ("Omega_3_Fatty_Acids_g", models.FloatField(blank=True, null=True)),
                ("Trans_Fatty_Acids_g", models.FloatField(blank=True, null=True)),
                (
                    "Total_Unsaturated_Fatty_Acids_g",
                    models.FloatField(blank=True, null=True),
                ),
                ("Ash_g", models.FloatField(blank=True, null=True)),
                ("Caffeine_mg", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
