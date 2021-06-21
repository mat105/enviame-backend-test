from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

from empresas.models import Company
from empresas.serializers import CompanySerializer


class CompanyTestCase(APITestCase):

    def test_get_companies(self):
        baker.make(Company)
        response = self.client.get('/companies/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data['results']
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        self.assertEqual(len(results), len(companies))
        self.assertEqual(len(companies), 1)
        self.assertEqual(results, serializer.data)

    def test_get_company(self):
        company = baker.make(Company, name='test_get_company')
        response = self.client.get(f'/companies/{company.id}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(name='test_get_company')
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)

    def test_get_company_throws_404_if_does_not_exists(self):
        total_companies = Company.objects.all().count()

        response = self.client.get(f'/companies/{total_companies+1}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_company(self):
        prev_companies_count = Company.objects.all().count()

        company = baker.prepare(Company, name='test_post_company')
        company_data = CompanySerializer(company).data

        response = self.client.post('/companies/', data=company_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        company = Company.objects.get(name='test_post_company')
        serializer = CompanySerializer(company)

        new_companies_count = Company.objects.all().count()

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(new_companies_count, prev_companies_count + 1)

    def test_delete_company(self):
        company = baker.make(Company, name='test_delete_company')

        response = self.client.delete(f'/companies/{company.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        companies_count = Company.objects.filter(name='test_delete_company').count()
        self.assertEqual(companies_count, 0)

    def test_put_company(self):
        company = baker.make(Company, name='test_put_company')

        data = CompanySerializer(company).data
        data['address'] = 'test_put_add_new_123'

        response = self.client.put(f'/companies/{company.id}/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(name='test_put_company')
        serializer = CompanySerializer(company)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(data, serializer.data)

    def test_patch_company(self):
        company = baker.make(Company)

        company_modify = {
            'address': 'patched'
        }

        response = self.client.patch(f'/companies/{company.id}/', data=company_modify, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        company = Company.objects.get(address='patched')
        serializer = CompanySerializer(company)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(company.address, company_modify['address'])
