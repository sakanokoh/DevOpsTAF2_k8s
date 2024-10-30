from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models, database

# Initialiser l'application FastAPI
app = FastAPI()

# Créer les tables dans la base de données
models.Base.metadata.create_all(bind=database.engine)

@app.get("/", response_description="Welcome to the FastAPI application")
def read_root():
    return {
        "message": "Bienvenue sur l'API FastAPI de Hamady SAKANOKO",
        "version": "1.0.0",
        "description": "Cette API permet de gérer les informations des étudiants. Vous pouvez créer, lire, mettre à jour et supprimer des informations sur les étudiants.",
        "endpoints": {
            "/students/": "Liste tous les étudiants",
            "/students/": "Créer un nouvel étudiant",
            "/students/{student_id}": "Lire les informations d'un étudiant spécifique",
            "/students/{student_id}": "Supprimer un étudiant spécifique"
        },
        "instructions": "Utilisez les endpoints ci-dessus pour interagir avec l'API. Assurez-vous de vérifier les documents et les modèles de données pour chaque point de terminaison.",
        
    }

# Endpoint readiness
@app.get("/health/ready", response_description="Readiness probe")
def readiness_probe():
    return {"status": "ready"}

# Endpoint liveness
@app.get("/health/live", response_description="Liveness probe")
def liveness_probe():
    return {"status": "alive"}

@app.get("/students/", response_description="List all students")
def list_students(db: Session = Depends(database.get_db)):
    students = db.query(models.Student).all()
    if students:
        return students
    return {"message": "No students found"}


# Schéma de validation des données d'entrée
class StudentCreateSchema(BaseModel):
    name: str
    age: int

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 22
            }
        }

@app.post("/students/", response_description="Student data added into the database")
async def create_student(student: StudentCreateSchema = Body(...), db: Session = Depends(database.get_db)):
    # Encoder les données pour qu'elles soient compatibles avec la base de données
    student_data = jsonable_encoder(student)
    new_student = models.Student(**student_data)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return student

@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
