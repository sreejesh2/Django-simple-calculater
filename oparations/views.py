from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'home.html')


class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "add.html")

    def post(self, request, *args, **kwargs):

        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = int(num1)+int(num2)
        context = {"answer": answer}
        return render(request, 'add.html', context)


class SubView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "sub.html")

    def post(self, request, *args, **kwargs):

        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = int(num1)-int(num2)
        context = {"answer": answer}
        return render(request, 'add.html', context)


class DivView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "div.html")

    def post(self, request, *args, **kwargs):

        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = float(num1)/float(num2)
        context = {"answer": answer}
        return render(request, 'add.html', context)


class MulView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mul.html")

    def post(self, request, *args, **kwargs):

        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = int(num1)*int(num2)
        context = {"answer": answer}
        return render(request, 'add.html', context)


class FactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fact.html')

    def post(self, request, *args, **kwargs):
        num = int(request.POST.get("num"))
        fact = 1
        # result=[fact*=i for i in range(1,num+1)]
        for i in range(1, num+1):
            fact *= i
        ans = fact
        context = {"answer": ans}
        return render(request, 'fact.html', context)


class PrimeNumberView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'prime.html')

    def post(self, request, *args, **kwargs):
        num = int(request.POST.get("num"))
        prime = any([num % i == 0 for i in range(2, num)])
        answer = 'not prime' if prime else 'prime'

        context = {"answer": answer}
        return render(request, 'prime.html', context)


class AmstrongNumberView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Amstong.html')

    def post(self, request, *args, **kwargs):
        num = int(request.POST.get("num"))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit**3
            temp //= 10
        answer = 'its amstrong' if num == sum else 'not amstrong'

        context = {"answer": answer}
        return render(request, 'amstong.html', context)


class PalindromeNumberView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'palin.html')

    def post(self, request, *args, **kwargs):
        num = int(request.POST.get("num"))
        rev = 0
        temp = num
        while (num > 0):
            digit = num % 10
            rev = rev*10+digit
            num=num // 10
      
        answer = 'its Palindrome' if temp == rev else 'not Palindrome'

        context = {"answer": answer}
        return render(request, 'palin.html', context)
