from django.db import models
from django.urls import reverse

from .pip import PIP
from .materials import Material

class Expense(models.Model):

    expense = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = ("Expense")
        verbose_name_plural = ("Expenses")

    def __str__(self):
        return self.expense

    def get_absolute_url(self):
        return reverse("Expense_detail", kwargs={"pk": self.pk})


class Budget(models.Model):

    pip = models.ForeignKey(PIP, on_delete=models.CASCADE)
    total_cost_material = models.IntegerField()
    total_cost_execution = models.IntegerField()
    total_cost_expense = models.IntegerField()

    class Meta:
        verbose_name = ("Budget")
        verbose_name_plural = ("Budgets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Budget_detail", kwargs={"pk": self.pk})

class MaterialBudget(models.Model):

    budge = models.ForeignKey(Budget, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_cost = models.IntegerField()
    total_cost = models.IntegerField()

    class Meta:
        verbose_name = ("MaterialBudget")
        verbose_name_plural = ("MaterialBudgets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MaterialBudget_detail", kwargs={"pk": self.pk})

class ExecutionBudget(models.Model):

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_cost = models.IntegerField()
    total_cost = models.IntegerField()

    class Meta:
        verbose_name = ("ExecutionBudget")
        verbose_name_plural = ("ExecutionBudgets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ExecutionBudget_detail", kwargs={"pk": self.pk})

class ExpenseBudget(models.Model):

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    rate = models.IntegerField()
    total_cost = models.IntegerField()

    class Meta:
        verbose_name = ("ExpenseBudget")
        verbose_name_plural = ("ExpenseBudgets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ExpenseBudget_detail", kwargs={"pk": self.pk})

