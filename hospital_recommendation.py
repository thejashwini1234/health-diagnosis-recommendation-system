from flask import Flask, request, render_template, Blueprint

# Initialize the Blueprint
hospital_recommendation = Blueprint('hospital_recommendation', __name__, template_folder="templates")

# Sample data: Dictionary mapping diseases to detailed hospital recommendations
hospital_data = {
    "allergy and immunology": [
      {"name": "Apollo BGS Hospitals, Mysuru", "Doctor": "Dr Madhu K","experience":"5+ Years Experience","contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
      {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
    
],

"audiology": [
    {"name": "Resonance Speech And Hearing Clinics", "contact": " 095380 55992", "website": "http://resonanceclinics.in/", "location": "https://www.google.com/maps?s=web&rlz=1C1JJTC_enIN1065IN1066&sca_esv=5430cf780e99fb8b&lqi=CiNSZXNvbmFuY2UgU3BlZWNoIGFuZCBIZWFyaW5nIENsaW5pY0iJ1NOvp7aAgAhaORAAEAEQAhADEAQYABgBGAIYAxgEIiNyZXNvbmFuY2Ugc3BlZWNoIGFuZCBoZWFyaW5nIGNsaW5pY5IBEnNwZWVjaF9wYXRob2xvZ2lzdKoBTBABMh8QASIbgX6o4GkNhtmu-9-8VFuftWW2vYbz__38s7IeMicQAiIjcmVzb25hbmNlIHNwZWVjaCBhbmQgaGVhcmluZyBjbGluaWM&phdesc=ZOp-mVWzH_I&vet=12ahUKEwjRsJ2Z85qKAxW-S2wGHR0hJQgQ1YkKegQILhAB..i&cs=1&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KRUSS1QsZa87Md1CF6Syu1_J&daddr=No.+L.+47,+Ground+Floor,+I+Stage,+Khb+Colony,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023"},
    {"name": "SphearWell - Speech & Hearing Center", "contact": "08511014976", "website": "https://www.justdial.com/Mysore/SphearWell-Speech-and-Hearing-Center-Near-Sharadadevi-Nagar-Circle-Sharadadevi-Nagar/0821PX821-X821-210215173020-E7Z4_BZDET", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWILCi6jF0tinzpDvYcziIeCebLYF1A:1733754601564&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiJlNwaGVhcldlbGwgLSBTcGVlY2ggYW5kIEhlYXJpbmcgQ2VudGVyMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMgUQABjvBTIIEAAYgAQYogRI6wVQAFgAcAB4AJABAJgB4AGgAeABqgEDMi0xuAEDyAEA-AEC-AEBmAIBoALjAZgDAJIHAzItMaAHjQg&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KY_jOht2e687MYTR5S9tO1gy&daddr=%23209,+First+Floor,+Sharadadevi+Nagar,+Circle,+Mysuru,+Karnataka+570022"}
        
],
"anesthesiology": [
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name":"Kamakshi Hospital Mysuru","contact":"+91 98456 42981" ,"website":"http://www.kamakshihospital.org/" ,"location":"https://www.google.com/maps/dir//Kamakshi+Hospital+Rd,+Kuvempunagara+North,+Kuvempu+Nagara,+Mysuru,+Karnataka+570009/@12.2998162,76.5413332,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7ab735a0053f:0x36b46e10756a3e7d!2m2!1d76.6237351!2d12.2998285?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
],
"ayurveda treatment":[
    {"name": "JSS Ayurvedic Medical College And Hospital", "contact": "0821 254 8360", "website": "https://jssamch.org/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWIKg1E0qajH8EqxJxD3Lx3F2GIzpfg:1733755085840&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2pzcyBheXVydmVkYSBob3NwaXRhbCBteXNvcmUgbG8qAggDMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAFIix1QgwJYvAtwAXgBkAEAmAHIAaABrASqAQUwLjIuMbgBAcgBAPgBAZgCBKACwATCAgoQABiwAxjWBBhHwgIFEAAYgATCAgsQLhiABBjHARivAcICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogSYAwCIBgGQBgiSBwUxLjIuMaAHjBg&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KfMqqPyPcK87MV374Z0lHMUx&daddr=%23+41/+E,+Lalithadripura+Road,+Mysuru,+Karnataka+570028"},
    {"name": "Amay INDIA - Atharva SuperMulti Speciality Ayurvedic Centre", "contact": "076769 29394", "website": "http://www.amayindia.in/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWIJ3DJ8d1DS4ImFx_HYi8sJV_GcNNg:1733755141216&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiO0FtYXkgSU5ESUEgLSBBdGhhcnZhIFN1cGVyTXVsdGkgU3BlY2lhbGl0eSBBeXVydmVkaWMgQ2VudHJlMgUQIRigAUiZBVAAWABwAHgAkAEAmAHeAaAB3gGqAQMyLTG4AQPIAQD4AQL4AQGYAgGgAuABmAMAkgcDMi0xoAeYAg&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KbN9-waqe687MTq2mPTpvQv2&daddr=1058,+Paduvana+Road,+New+Kantharaj+Urs+Rd,+opposite+JK+tyre,+TK+Layout+4th+Stage,+Saraswathipuram,+Mysuru,+Karnataka+570023"}
    
],
"cardiology": [
        {"name": "Apollo BGS Hospitals, Mysuru","Doctor":"Dr. Guru Prasad B V","experience":"12+years", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name":"Kamakshi Hospital Mysuru","contact":"+91 98456 42981" ,"website":"http://www.kamakshihospital.org/" ,"location":"https://www.google.com/maps/dir//Kamakshi+Hospital+Rd,+Kuvempunagara+North,+Kuvempu+Nagara,+Mysuru,+Karnataka+570009/@12.2998162,76.5413332,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7ab735a0053f:0x36b46e10756a3e7d!2m2!1d76.6237351!2d12.2998285?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
],
"dental":[
    {"name": "JSS Dental College and Hospital", "contact": "0821 254 8349", "website": "https://jsshospital.in/specialities/dental/", "location": "https://www.google.com/maps/dir//jss+dental+hospital+mysore+timings/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf7085f15b03a5:0x36e22c7750c2fa4c?sa=X&ved=1t:3061&ictx=111"},
    {"name": "Apollo Dental Clinic, Mysore BGS","Doctor":"Dr Keerthana Dr","experience":"9 years", "contact": "1800 102 0288", "website": "https://apollodental.in/mysuru/our-clinics", "location": "https://www.google.com/maps/dir//Apollo+Dental+Clinic,+Mysuru+-+Best+Dental+Clinic+in+Bengaluru+-+Root+Canals,+Aligners,+Implants,+Crowns+and+Veneers,+Apollo+BGS+Hospitals,+Adichunchanagiri+Road+,Kuvempunagar,+Mysuru,+Karnataka+570023/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf655261e40e57:0x9e6bc9fa5573f7bd?sa=X&ved=1t:57443&ictx=111"}
],
"dermatology": [
        {"name": "Cutie pie clinic", "contact": "097404 67263", "website": "http://www.cutiepieclinic.com/", "location": "https://www.google.com/maps/dir//664%2Fa,+Kamakshi+Hospital+Rd,+Saraswathipuram,+Mysuru,+Karnataka+570009/@12.2999445,76.5440441,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7b50f720242d:0xb41570eb93c5059!2m2!1d76.626446!2d12.2999568?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Sundew Cosmetic Surgery & Hair Transplant Centre", "contact": "0821 424 2294", "website": "http://www.sundewcosmetic.com/", "location": "https://www.google.com/maps?sca_esv=293021c43ebdc58d&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIKE6EowoAtqpYWzF6VrWT2KLCf0hA:1733319668135&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiO1N1bmRldyBDb3NtZXRpYyBTdXJnZXJ5IGFuZCBIYWlyIFRyYW5zcGxhbnQgQ2VudHJlLiA1LjAuIC4uMgUQIRigAUj7C1DHBljHBnABeACQAQCYAeoCoAHqAqoBAzMtMbgBA8gBAPgBAfgBApgCAqAC-wKoAhTCAgcQIxgnGOoCwgINEC4YxwEYJxjqAhivAcICEBAuGMcBGCcY6gIYjgUYrwHCAg0QLhjRAxjHARgnGOoCwgIQEAAYAxi0AhjqAhiPAdgBAZgDDLoGBggBEAEYCpIHBTEuMy0xoAeYAg&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KetAOAobcK87MYEzKPxvWqK-&daddr=63,+4th+floor,+SUNDEW+Complex,+opp.+JSS+Hospital+Road,+Agrahara,+Chamrajpura,+Mysuru,+Karnataka+570004"}
],
"emergency medicine": [
        {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
],
"endocrinology": [
        {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Udupa Clinic", "contact": "082777 01314", "website": "https://www.justdial.com/Mysore/Udupa-Clinic-Opposite-to-Hoysala-Karnataka-Sangha-Kr-Mohalla/0821PX821-X821-170202002214-W8H7_BZDET", "location": "https://www.google.com/maps?rlz=1C1JJTC_enIN1065IN1066&gs_lcrp=EgZjaHJvbWUqEAgCEC4YrwEYxwEYgAQYjgUyCggAEEUYFhgeGDkyDQgBEC4YrwEYxwEYgAQyEAgCEC4YrwEYxwEYgAQYjgUyBwgDEAAYgAQyCAgEEAAYFhgeMgoIBRAAGAoYFhgeMgoIBhAAGAoYFhgeMgoIBxAAGAoYFhgeMgoICBAAGAoYFhge0gEJNjc3OGowajE1qAIIsAIB&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KZkTV_ADcK87MX-Cqi0lmQIv&daddr=1638,+%E0%B2%A8%E0%B2%BE%E0%B2%B0%E0%B2%BE%E0%B2%AF%E0%B2%A3+%E0%B2%B6%E0%B2%BE%E0%B2%B8%E0%B3%8D%E0%B2%A4%E0%B3%8D%E0%B2%B0%E0%B2%BF+%E0%B2%B0%E0%B2%B8%E0%B3%8D%E0%B2%A4%E0%B3%86,+NR+Mohalla,+Lakshmipuram,+Mysuru,+Karnataka+570004"}
],
"gastroenterology": [
        {"name": "N J Hospital-Mysore Institute Of Gastro Enterology", "contact": "07041968102", "website": "https://www.justdial.com/Mysore/N-J-Hospital-Mysore-Institute-Of-Gastro-Enterology-Vinayakanagar-Jayalakshmipuram/0821PX821-X821-240229193407-R3A1_BZDET", "location": "https://www.google.com/maps/dir//N+J+Hospital-Mysore+Institute+Of+Gastroenterology/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf7bcad37cc317:0xe5eb1bada34edd89?sa=X&ved=1t:3061&ictx=111"},
        {"name": "Nayana Kumar's Multi Speciality Hospital, Mysuru", "contact": "095133 10100", "website": "https://www.nkhospitals.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIIQYbfw6NG4PtDIS9ly9jq5c_-xDQ:1733750915875&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiKE5heWFuYSBLdW1hcidzIE11bHRpIFNwZWNpYWxpdHkgSG9zcGl0YWwyCxAuGIAEGMcBGK8BMgUQABiABDIKEAAYgAQYQxiKBTIIEAAYFhgKGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyGhAuGIAEGMcBGK8BGJcFGNwEGN4EGOAE2AEBSJwbUOMUWOMUcAJ4AJABAJgBwgKgAfYDqgEHMC4xLjAuMbgBA8gBAPgBAfgBApgCA6AC-wKoAhTCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICBxAjGCcY6gLCAhAQLhjHARgnGOoCGI4FGK8BwgIQEAAYAxi0AhjqAhiPAdgBAcICEBAuGAMYtAIY6gIYjwHYAQGYAyLiAwUSATEgQPEF6Pf7d9olD5aIBgGQBga6BgYIARABGAqSBwUyLjMtMaAHpBI&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KVNagC1Xca87MRwtqFYBgeFX&daddr=No+6,+3rd+Main+Rd,+near+Nethaji+Circle,+Dattagalli,+Rajajinagara,+Rajarajeshwari+Nagar,+Mysuru,+Karnataka+570022"},

],
"general surgery": [
        {"name": "GCs Sports medicine & Multispeciality Hospital", "contact": "0821 4000108", "website": "https://girishchandrahospital.com/", "location": "https://www.google.com/maps/dir//GC%E2%80%99s+Sports+medicine+%26+Multispeciality+Hospital,+GS+Ramakrishnaiah+Main+Rd,+Vidyaranyapura,+Visveshwara+Nagar,+Karnataka+570008/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf6fe311f6f533:0x4fb5099dcfbc8685?sa=X&ved=1t:57443&ictx=111"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
],
"geriatrics": [
        {"name": "Narayana Hospital, Mysore", "contact": "098539 98539", "website": "https://www.narayanahealth.org/hospitals/mysore/narayana-multispeciality-hospital-mysore/?utm_source=Googlemaps&utm_medium=GMB", "location": "https://www.google.com/maps/dir//Narayana+Hrudayalaya+Surgical+Hospital+Pvt+Ltd/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71a12b5ff6e3:0xfa137a5dcf03a77b?sa=X&ved=1t:3061&ictx=111"},
        {"name": "Lakshya Geriatric(elderly care) Clinic", "contact": " 093532 71649", "website": "https://www.justdial.com/Mysore/Lakshya-Geriatric-elderly-Care-Clinic-DR-Shilpa-Avarebeel-Next-to-Kumar-Medicals-Kuvempunagar/0821PX821-X821-211013191241-A7V4_BZDET", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWILQDWRdOfX8slNuBcv2duGPmIwHCg:1733751288363&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiPExha3NoeWEgR2VyaWF0cmljIChlbGRlcmx5IENhcmUpIENsaW5pYyAoRFIgU2hpbHBhIEF2YXJlYmVlbDIFEAAY7wUyCBAAGIAEGKIEMggQABiABBiiBDIFEAAY7wUyCBAAGIAEGKIESPsDUABYAHAAeACQAQCYAa0DoAGtA6oBAzQtMbgBA8gBAPgBAvgBAZgCAaACswOYAwCSBwM0LTGgB5cD&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=Kbv3fe3GZa87Md-NcFZLPkvW&daddr=Mallyas+Empire,+108/1,+Panchamantra+Rd,+next+to+Kumar+Medicals,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023"}

],
"hair transplant":[
    {"name": "Sundew Cosmetic Surgery & Hair Transplant Centre", "contact": "0821 424 2294", "website": "http://www.sundewcosmetic.com/", "location": "https://www.google.com/maps?sca_esv=293021c43ebdc58d&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIKE6EowoAtqpYWzF6VrWT2KLCf0hA:1733319668135&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiO1N1bmRldyBDb3NtZXRpYyBTdXJnZXJ5IGFuZCBIYWlyIFRyYW5zcGxhbnQgQ2VudHJlLiA1LjAuIC4uMgUQIRigAUj7C1DHBljHBnABeACQAQCYAeoCoAHqAqoBAzMtMbgBA8gBAPgBAfgBApgCAqAC-wKoAhTCAgcQIxgnGOoCwgINEC4YxwEYJxjqAhivAcICEBAuGMcBGCcY6gIYjgUYrwHCAg0QLhjRAxjHARgnGOoCwgIQEAAYAxi0AhjqAhiPAdgBAZgDDLoGBggBEAEYCpIHBTEuMy0xoAeYAg&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KetAOAobcK87MYEzKPxvWqK-&daddr=63,+4th+floor,+SUNDEW+Complex,+opp.+JSS+Hospital+Road,+Agrahara,+Chamrajpura,+Mysuru,+Karnataka+570004"},
    {"name": "Reniu Skin, Cosmetology, Laser", "contact": " 089771 14111", "website": "https://www.reniuclinic.com/fue-hair-transplant/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWIL0B77M8zY9Imfi7yA0GcptRMHZCw:1733754822624&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIgRyZW5pKgIIADIQEC4YgAQYQxjHARiKBRivATIOEC4YgAQYsQMYxwEYrwEyCBAAGIAEGLEDMggQABiABBixAzIFEAAYgAQyCBAAGIAEGLEDMggQLhiABBixAzIFEC4YgAQyBRAAGIAEMgUQLhiABDIfEC4YgAQYQxjHARiKBRivARiXBRjcBBjeBBjgBNgBAUiqPlAAWMkocAF4AJABAJgBwQGgAfYGqgEDMC41uAEByAEA-AEBmAIHoALlE8ICChAjGIAEGCcYigXCAgQQIxgnwgILEC4YgAQYkQIYigXCAhEQLhiABBiRAhjHARiKBRivAcICERAuGIAEGLEDGNEDGIMBGMcBwgIOEC4YgAQYsQMY0QMYxwHCAhQQABiABBixAxiDARiKBRiLAxiMBsICChAAGIAEGEMYigXCAg0QABiABBixAxhDGIoFwgILEAAYgAQYkQIYigXCAgsQLhiABBixAxjUAsICEBAuGIAEGNEDGEMYxwEYigWYAwC6BgYIARABGBSSBwkxLjQuMS43LTGgB5tQ&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=Kf_IfieQeq87MTzNwuLuD7Mt&daddr=2714/D1,+Kalidasa+Road,+8th+Cross+Rd,+adjacent+empire+hotel,+Vani+Vilas+Mohalla,+Mysuru,+Karnataka+570002"}
    
],

"homeopathy": [
    {"name": "Namma Homeopathy", "contact": "099000 91777", "website": "https://nammahomeopathy.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWIIindJR0nLmxvi6gOdp4q2cxutBPw:1733755186143&gs_lp=Egxnd3Mtd2l6LXNlcnAiEW5hbW1hIGhvbWVvcGF0aHkgKgIIADIQEC4YgAQYFBiHAhjHARivATIREC4YgAQYkgMYxwEYjgUYrwEyCBAAGIAEGMkDMg4QABiABBiRAhiSAxiKBTIFEAAYgAQyCxAAGIAEGJECGIoFMgsQLhiABBjHARivATILEC4YgAQYxwEYrwEyCxAuGIAEGMcBGK8BMgoQABiABBgUGIcCMh8QLhiABBgUGIcCGMcBGK8BGJcFGNwEGN4EGOAE2AEBSMo3UABYkS9wAHgAkAEAmAHaAaABmBeqAQYwLjE0LjO4AQHIAQD4AQGYAhGgAoIYwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBixAxiDAcICERAuGIAEGLEDGNEDGIMBGMcBwgILEC4YgAQYsQMYgwHCAgsQLhiABBjRAxjHAcICChAuGIAEGEMYigXCAgoQABiABBhDGIoFwgINEC4YgAQYsQMYQxiKBcICCBAAGIAEGLEDwgIOEAAYgAQYsQMYgwEYigXCAg4QLhiABBixAxjRAxjHAcICDhAuGIAEGMcBGI4FGK8BwgIUEC4YgAQYsQMYgwEYxwEYjgUYrwHCAg0QABiABBixAxhDGIoFwgIREC4YgAQYkQIYxwEYigUYrwHCAggQABiABBiSA8ICCBAuGIAEGNQCmAMAugYGCAEQARgUkgcGMC4xMy40oAf9vwI&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=Kb-V0eMVca87MXWdoutROlfP&daddr=No.27/1,+1st+Floor,+Opp.+Small+Clock+Tower,+Shivarampet,+Mysuru,+Karnataka+570001"},
    {"name": "Homeocare International Mysore | Homeopathy Clinic", "contact": "1800 102 2202", "website": "https://www.homeocare.in/", "location": "https://www.google.com/maps/dir//Homeocare+International+Mysore+%7C+Homeopathy+Clinic+-+Mysore(Mysuru),+Dodda+Gadiyara,+Opp:,+Ashoka+Rd,+above+Corporation+Bank+-+Main+Branch,+Mysuru,+Karnataka+570002/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf700df15851e3:0x52eac0818572d01a?sa=X&ved=1t:57443&ictx=111"}
    
],
"hematology": [
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Narayana Hospital, Mysore", "contact": "098539 98539", "website": "https://www.narayanahealth.org/hospitals/mysore/narayana-multispeciality-hospital-mysore/?utm_source=Googlemaps&utm_medium=GMB", "location": "https://www.google.com/maps/dir//Narayana+Hrudayalaya+Surgical+Hospital+Pvt+Ltd/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71a12b5ff6e3:0xfa137a5dcf03a77b?sa=X&ved=1t:3061&ictx=111"}
],
"infectious disease": [
    {"name": "Udupa Clinic", "contact": "082777 01314", "website": "https://www.justdial.com/Mysore/Udupa-Clinic-Opposite-to-Hoysala-Karnataka-Sangha-Kr-Mohalla/0821PX821-X821-170202002214-W8H7_BZDET", "location": "https://www.google.com/maps?rlz=1C1JJTC_enIN1065IN1066&gs_lcrp=EgZjaHJvbWUqEAgCEC4YrwEYxwEYgAQYjgUyCggAEEUYFhgeGDkyDQgBEC4YrwEYxwEYgAQyEAgCEC4YrwEYxwEYgAQYjgUyBwgDEAAYgAQyCAgEEAAYFhgeMgoIBRAAGAoYFhgeMgoIBhAAGAoYFhgeMgoIBxAAGAoYFhgeMgoICBAAGAoYFhge0gEJNjc3OGowajE1qAIIsAIB&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KZkTV_ADcK87MX-Cqi0lmQIv&daddr=1638,+%E0%B2%A8%E0%B2%BE%E0%B2%B0%E0%B2%BE%E0%B2%AF%E0%B2%A3+%E0%B2%B6%E0%B2%BE%E0%B2%B8%E0%B3%8D%E0%B2%A4%E0%B3%8D%E0%B2%B0%E0%B2%BF+%E0%B2%B0%E0%B2%B8%E0%B3%8D%E0%B2%A4%E0%B3%86,+NR+Mohalla,+Lakshmipuram,+Mysuru,+Karnataka+570004"},
    {"name": "DSC Healthcare", "contact": " 088842 51781", "website": "http://dschealthcare.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIIhrhxsJtBZwOe10npgDCm1Q7bqRw:1733752017944&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiD0RTQyBIZWFsdGggQ2FyZTIOEC4YgAQYxwEYjgUYrwEyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMh0QLhiABBjHARiOBRivARiXBRjcBBjeBBjgBNgBAUisA1AAWABwAHgAkAEAmAGgAqABoAKqAQMyLTG4AQPIAQD4AQL4AQGYAgGgAq0CmAMAugYGCAEQARgUkgcDMy0xoAfZCA&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KRnV--Vpca87MXl0uXcP-QM8&daddr=88/2B,+Jattipalla+-+Kanakapura+Rd,+Mysuru,+Karnataka+570029"}
        
],
"internal medicine": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
        
],
"nephrology": [
    {"name": "The Academy of Universal Acupuncture Edu Trust & Healthcare", "contact": "095665 04571", "website": "https://www.justdial.com/Mysore/The-Universal-Acupuncture/0821PX821-X821-201117155845-G3G2_BZDET", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWILQ-HJqvac8CSChsKpm3VfIRY6dnw:1733752065450&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ1RoZSBVbml2ZXJzYWwgQWN1cHVuY3R1cmUgJiBFZHUuIFRydXN0LjIGEAAYFhgeMgYQABgWGB4yBRAAGO8FMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMgUQABjvBUicBlAAWABwAHgAkAEAmAGAAqABgAKqAQMyLTG4AQPIAQD4AQL4AQGYAgGgAocCmAMAkgcDMi0xoAebBQ&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KeXDKyeqe687McUSf3EdmaF7&daddr=2165,+2nd+cross,+Basaveshwara+Rd,+near+101+Ganapathi+Temple,+Agrahara,+KR+Mohalla,+Mysuru,+Karnataka+570004"},
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
        
],
"neurology": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
        
        
],
"obstetrics and gynecology": [
    {"name": "Kangaroo Care - Women and Children Hospital in Mysore", "contact": "1800 425 4500", "website": "https://kangaroocareindia.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIJJec-F1sb9jH9Cn0JUXnqHcrAO5A:1733752215254&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiMEthbmdhcm9vIENhcmUgV29tZW4gYW5kIENoaWxkcmVuIEhvc3BpdGFsIE15c29yZTIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyBRAAGO8FMggQABiABBiiBEi3A1AAWABwAHgAkAEAmAHRAqAB0QKqAQMzLTG4AQPIAQD4AQL4AQGYAgGgAtcCmAMAkgcDMy0xoAekBQ&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KS1sFOX4e687MbtncC3xdj2U&daddr=%23505,+Kalidasa+Rd,+opp.+MUDA+Commercial+complex,+Vijayanagar+1st+Stage,+Vijayanagar,+Mysuru,+Karnataka+570017"},
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
        
],
"oncology": [
    {"name": "Mysore Institute of Gastroenterology", "contact": "08460489828", "website": "https://www.justdial.com/Mysore/Mysore-Institute-Of-Gastro-Enterology-Hunsur-Bypass-Road-Yelwal/0821PX821-X821-231006113148-H2Y3_BZDET", "location": "https://www.google.com/maps/dir//Mysore+Institute+Of+Gastroenterology/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf7bcad37cc317:0xe5eb1bada34edd89?sa=X&ved=1t:3061&ictx=111"},
    {"name": "prakash ent & cancer care clinic", "contact": "080 4696 1835", "website": "https://www.wellnessvibesclinic.com/", "location": "https://www.google.com/maps/dir//prakash+ent+%26+cancer+care+clinic/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3bae73f5c7e52ad9:0x1df3df748d5c6d0b?sa=X&ved=1t:3061&ictx=111"}
        
],
"ophthalmology": [
    {"name": "ASG Eye Hospital", "contact": "1800 1200 111", "website": "https://asgeyehospital.com/hospitals/mysore", "location": "https://www.google.com/maps/dir//ASG+Eye+Hospital/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf719740d3d77f:0x1cf69cb65a42edd0?sa=X&ved=1t:3061&ictx=111"},
    {"name": "Dr Agarwals Eye Hospital", "contact": "080 4819 3490", "website": "https://www.dragarwal.com/eye-hospital/kuvempunagara/?utm_source=locator&utm_medium=googleplaces", "location": "https://www.google.com/maps/dir//No+1792,+Ward,+Dr+Agarwals+Eye+Hospital,+Near+Jayamma+Govindegowda+Choultry,+18,+Adichunchanagiri+Road,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf65526958e50d:0xfff86104a036e2c6?sa=X&ved=1t:57443&ictx=111"}
],
"orthopedics": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
          
],
"pediatrics": [
    {"name": "Nayana Kumar's Multi Speciality Hospital", "contact": "095133 10100", "website": "https://www.nkhospitals.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWILo7aMGbWxhhe62r_St3LTfxaMudw:1733753205130&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiKE5heWFuYSBLdW1hcidzIE11bHRpIFNwZWNpYWxpdHkgSG9zcGl0YWwyChAjGIAEGCcYigUyCxAuGIAEGMcBGK8BMgUQABiABDIIEAAYFhgKGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogRIiAZQAFgAcAB4AJABAJgB6AGgAegBqgEDMi0xuAEDyAEA-AEC-AEBmAIBoALtAZgDAJIHAzItMaAHnQ8&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KVNagC1Xca87MRwtqFYBgeFX&daddr=No+6,+3rd+Main+Rd,+near+Nethaji+Circle,+Dattagalli,+Rajajinagara,+Rajarajeshwari+Nagar,+Mysuru,+Karnataka+570022"},
    {"name": "Kangaroo Care - Women and Children Hospital in Mysore", "contact": "1800 425 4500", "website": "https://kangaroocareindia.com/", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&sxsrf=ADLYWIJJec-F1sb9jH9Cn0JUXnqHcrAO5A:1733752215254&uact=5&gs_lp=Egxnd3Mtd2l6LXNlcnAiMEthbmdhcm9vIENhcmUgV29tZW4gYW5kIENoaWxkcmVuIEhvc3BpdGFsIE15c29yZTIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyBRAAGO8FMggQABiABBiiBEi3A1AAWABwAHgAkAEAmAHRAqAB0QKqAQMzLTG4AQPIAQD4AQL4AQGYAgGgAtcCmAMAkgcDMy0xoAekBQ&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KS1sFOX4e687MbtncC3xdj2U&daddr=%23505,+Kalidasa+Rd,+opp.+MUDA+Commercial+complex,+Vijayanagar+1st+Stage,+Vijayanagar,+Mysuru,+Karnataka+570017"}
        
],
"plastic surgery": [
    {"name": "jss hospital", "contact": "0821-2335555", "website": "https://jsshospital.in/specialities/plastic-surgery/", "location": "https://www.google.com/maps/dir//JSS+Hospital+Mysore,+Mahatma+Gandhi+Road,+Fort+Mohalla,+Mysuru,+Karnataka+570004/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71b30c0a2ae3:0x2981a75406bdcce9?sa=X&ved=1t:57443&ictx=111"},
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
        
],
"psychiatry": [
        {"name": "Prerana Hospital- Psychiatrist Hospital in Mysuru", "contact": "+91 72042 70871", "website": "https://preranahospitalmysore.com/psychiatry", "location": "https://www.google.com/maps?sca_esv=5430cf780e99fb8b&rlz=1C1JJTC_enIN1065IN1066&biw=1536&bih=730&sxsrf=ADLYWIKMYuv80YSiKCdu3p9u52qjGsklow:1733753840227&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIgdwcmVyYW5hKgIIATIKEAAYgAQYQxiKBTIQEC4YgAQYQxjHARiKBRivATILEC4YgAQYsQMYgwEyChAAGIAEGEMYigUyDhAuGIAEGMcBGI4FGK8BMggQABiABBixAzIQEC4YgAQYQxjHARiKBRivATIKEAAYgAQYQxiKBTIFEAAYgAQyCBAuGIAEGLEDMh8QLhiABBhDGMcBGIoFGK8BGJcFGNwEGN4EGOAE2AEBSLsaUABYzxFwAHgBkAEAmAGZAqAB4A2qAQMyLTe4AQHIAQD4AQGYAgigApQTwgIEECMYJ8ICDhAuGIAEGLEDGIMBGIoFwgIREAAYgAQYsQMYgwEYigUYjAbCAg4QABiABBixAxiDARiKBcICCxAAGIAEGLEDGIMBwgIKECMYgAQYJxiKBcICDRAuGIAEGLEDGEMYigXCAhAQLhiABBixAxhDGIMBGIoFwgINEAAYgAQYsQMYQxiKBZgDALoGBggBEAEYFJIHBzItNy41LTGgB-F2&um=1&ie=UTF-8&fb=1&gl=in&sa=X&geocode=KXvF1jhLZa87MfYfCgDgqFPm&daddr=Water+tank,+452,+Paduvana+Road,+Landmark:,+Kuvempunagara+North,+TK+Layout,+Mysuru,+Karnataka+570009"},
        {"name": "jss hospital", "contact": "0821-2335555", "website": "https://jsshospital.in/specialities/psychiatry/", "location": "https://www.google.com/maps/dir//JSS+Hospital+Mysore,+Mahatma+Gandhi+Road,+Fort+Mohalla,+Mysuru,+Karnataka+570004/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71b30c0a2ae3:0x2981a75406bdcce9?sa=X&ved=1t:57443&ictx=111"},
],
"pulmonology": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
         
],

"radiology": [
    {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
    {"name": "jss hospital", "contact": "0821-2335555", "website": "https://jsshospital.in/specialities/psychiatry/", "location": "https://www.google.com/maps/dir//JSS+Hospital+Mysore,+Mahatma+Gandhi+Road,+Fort+Mohalla,+Mysuru,+Karnataka+570004/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71b30c0a2ae3:0x2981a75406bdcce9?sa=X&ved=1t:57443&ictx=111"}
],

"rheumatology": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
        {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
    
],

"urology ": [
    {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
    {"name": "jss hospital", "contact": "0821-2335555", "website": "https://jsshospital.in/specialities/urology/", "location": "https://www.google.com/maps/dir//JSS+Hospital+Mysore,+Mahatma+Gandhi+Road,+Fort+Mohalla,+Mysuru,+Karnataka+570004/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3baf71b30c0a2ae3:0x2981a75406bdcce9?sa=X&ved=1t:57443&ictx=111"}
],

"vascular surgery": [
    {"name": "Apollo BGS Hospitals, Mysuru", "contact": "+91 8069991025", "website": "https://www.apollohospitals.com/mysore/", "location": "https://www.google.com/maps/dir//Adichunchanagiri+Road,+Jayanagar,+Kuvempu+Nagara,+Mysuru,+Karnataka+570023/@12.2959517,76.5501357,12z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7aab67734a87:0x9a88cfb78df5e7c7!2m2!1d76.6325376!2d12.295964?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"},
    {"name": "Manipal Hospital Mysore", "contact": "+1800 102 4647", "website": "https://www.manipalhospitals.com/mysore/", "location": "https://www.google.com/maps/dir//No.+85-86,+Bangalore-Mysore+Ring+Road+Junction+Bannimantapa+'A'+Layout,+Siddique+Nagar,+Mandi+Mohalla,+Mysuru,+Karnataka+570015/@12.3652785,76.5245732,11.19z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3baf7092496f2c85:0xd84f0cc826a451aa!2m2!1d76.6601803!2d12.3499753?entry=ttu&g_ep=EgoyMDI0MTIwMS4xIKXMDSoASAFQAw%3D%3D"}
    
]

}

# Blueprint routes
@hospital_recommendation.route('/')
def hospital_recommendation_home():
    return render_template('hospital_recommendation.html', hospital_data=hospital_data)

@hospital_recommendation.route('/recommend', methods=['GET'])
def recommend_hospital():
    disease = request.args.get('disease', '').lower()
    recommended_hospitals = hospital_data.get(disease, [])
    return render_template(
        'hospital_recommendation.html', 
        hospital_data=hospital_data,
        selected_disease=disease,
        recommended_hospitals=recommended_hospitals
    )

# Create Flask App
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(hospital_recommendation, url_prefix='/hospital_recommendation')

# Main app route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
