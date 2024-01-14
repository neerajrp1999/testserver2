import firebase_admin
from firebase_admin import credentials, messaging
from google.cloud import firestore
from django.http import JsonResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
l={
  "type": "service_account",
  "project_id": "matrimonial-app-android",
  "private_key_id": "df71af14b9cc88cda4d0bc7a981e656d3d740997",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCKgZkGINgIAzAh\n+6zNjPDVa0iKTWKYYuitCDrYt76Sqe12wcNdrFSmXFarC3ZKTpKLZq1M1uJFHNTm\nCS6C/MpMtQGDSO7MyFGNDdEAyHPhoio3Mh5ZXQDWtUdBbdhCVcWhcsOZyloP25Kf\nkfzGZs/c1q4wpqkp/ujSLRE0EUc0Zy/OcVEIfcC8WNmKvkG97Zo+W3BakjwOHomF\nJvMjiJDavu/lHkqhO5GR3CVfitxmh+HmTVey+7DCzlmKSlOsmtOtqv83RwhoFfMp\ngTuz+pculRhffgp8OZIcYry0dUPSgwWf2LZIFbU7qkuRGruNUdIRlYadrv55g9uN\nWtkxL6y9AgMBAAECggEACsnU8kgBI8Ch0WfR2jHp+WmxnQoxjZaYso+jS8mmJ7Ti\nOP+XONbpQgsLuid6p4eOvRp6kbNkLQd1otRgwdWwaUCpFUGLTjqlNYQ3vSSf+BmC\nScnW2NWYcODuY6+LaoFVU0HF8Bb1pGoRNeowYwDTnItBRqtYnluLZYGapzBYWEG6\n/rkCHbiP24aZordFTWdEjroHs77wXKql+fIXCCJ4/X4GZC+CYhztZ8+s3ztyaIm3\nTxqdv0I2h03Yhr1kGtLnV3rbfnPTSa6UMv64RUlTzlG518k5yX5Euf02dBR2pztg\nEPNKCa74OinI4H4dhM7h5CXE56y47EB7EJ77fBNfuQKBgQC+V+MXdjJxem58d5o6\nQ8vmuKK7G14UEtUllRG/MMVNf2J5dayjCu2+FFgxKN+fJsRLjjjAWL6XQCyQ6tGQ\nW+S4y53FSqXSIspyoWqFHL/J0vqbH57anRHYOgGwxVrWZW+ACjvL7udY3MWhxwAu\nOF9XpscZK3XYHRjC1Xj7F5eH1QKBgQC6SEeyqH0ndaWM8GRVExI4N8XAGllzCZDy\nRQHoubrrZYpuLNm/rYHxZHY3ZK1wU7RmUpFYYjoZ8r9Hr0Ko2cgc5RNiJ1awxc8z\nRdU63AEwPrp2wSp+whp2jvI09Dw0MiMD+2xlgQl0ktjtIExf+b4zNB96k1phpsHQ\nYqBBHfOtSQKBgQCLnN8+6D1bqte7h+ah8fRvSOJjp1E8HAwnQs3/lIBDtbm/KSb1\neCClmTqO5FIR5Fd6q9jIjM9PFY0axoHsBtsfCIqymWxDU612oxsEg+/Q02Vpvqm/\n5BGgrftrc3aLZ19/ZQIzNQqPzW9QmCxzunmESxoiRhRr7fupfPb+BXHp+QKBgQCi\n8MhuOLzIgDqfzkIkvDrKm9ZIk4O8gRidIclqtNMQRlBQ0MBizjUEXfiduV2QDFeW\nzRA/fCQQQGoaHO403dIRnDpZN8m3dD8qPSInivsrJSNa7tnp6ITXQXAQ67Whfl1s\nhUaqfrUzl6NRv1eu97fr9+K1CCEdm4yaZzp/2uAjqQKBgH7ueeTr3WspZcFu9U/g\nYhJ+Sr02nJHiF6dgFLOeYikNnd1pC95vqGAyxQ/fKLQbM6OT2jJcBV/z67n74qci\nOvOzVWzCUJv2pt+llju/tkqPYyI/p7MeUPf08a8XhZeg6GGsK3SgwCyr89NiXF8d\nmQl4BBaCgDKc6cKqq9w1tXts\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-gjij5@matrimonial-app-android.iam.gserviceaccount.com",
  "client_id": "115827954528167079848",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gjij5%40matrimonial-app-android.iam.gserviceaccount.com"
}



cred = credentials.Certificate(l)
firebase_admin.initialize_app(cred)

def dataUrl(phoneNO):
    db=firestore.client()
    result = db.collection('Users').document(phoneNO).get().get('Profile').get('imageUri')[0]
    return result    
    
def sendPush(title, msg, registration_token, dataObject=None):
    
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )
    
    response = messaging.send_multicast(message)
    return response