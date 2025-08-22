import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client(database_id='database-id')


def creating_data():
    # "analytics" adında collection ve "stats" adında document oluşturuyoruz
    doc_ref = db.collection("analytics_demo").document("stats")

    data = {
        "main characters": {
            "carl johnson": {
                "job": "taxi driver",
                "age": 22,
                "gender": "male"
            }
        }
    }

    doc_ref.set(data)  # collection yoksa otomatik açılır, yoksa güncellenir
    print("Collection ve document oluşturuldu!")


def reading_data():
    doc_ref = db.collection("analytics_demo").document("stats")
    doc = doc_ref.get()
    if doc.exists:
        print("Document data:", doc.to_dict())
    else:
        print("No such document!")


def updating_data():
    doc_ref = db.collection("analytics_demo").document("stats")
    doc_ref.update({
        "main characters.carl johnson.age": 23
    })
    print("Document updated!")


def deleting_data():
    doc_ref = db.collection("analytics_demo").document("stats")
    doc_ref.delete()
    print("Document deleted!")


if __name__ == "__main__":
    creating_data()
    updating_data()
    reading_data()
    deleting_data()

