import requests
import json
import codecs

def filterArray(filterValue, originalArray):
	filtered = []
	for item in originalArray:
		print("ola")


def main():
	info_array = {
		"country": "Guatemala",
		"currency": "Quetzales",
		"departments":[],
		"resumeInfo":[]
		}
	req_dep = requests.get('https://capaportaldatosabiertos.mingob.gob.gt/api/dataset/7f3ea5e50ea1b9ab7e988eade7b29dbc')
	departments_response = req_dep.json()
	req = requests.get('https://capaportaldatosabiertos.mingob.gob.gt/api/dataset/f6617c3442570adc6d3ce60517ee3ee1')
	municipalities_response = req.json()
	municipalities_list = municipalities_response['result']['data'][0]

	departments_info_array = []
	counter = 0
	for department in departments_response["result"]["data"][0]:
		departments_info_array.append({
			"department_id": counter,
			"department_name": department[""]
		})
		counter+= 1

	for department in departments_info_array:
		selected_department_municipalities = []
		for municipality in municipalities_list:
			if municipality["codigo_departamento"] == department["department_id"]:
				selected_department_municipalities.append(municipality["nombre_municipio"])
				tempString = department["department_name"]+ "," + municipality["nombre_municipio"]
				info_array["resumeInfo"].append(tempString)
		info_array["departments"].append({
			"departmentName": department["department_name"],
			"municipalities": selected_department_municipalities
		})
	with codecs.open("departments_info.json", 'w', encoding='utf-8') as file:
		json.dump(info_array, file, ensure_ascii=False)


if __name__ == '__main__':
    main()