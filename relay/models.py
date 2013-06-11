# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AccGlAccount(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=135)
    parent = models.ForeignKey('self', null=True, blank=True)
    gl_code = models.CharField(max_length=135, unique=True)
    disabled = models.IntegerField()
    manual_journal_entries_allowed = models.IntegerField()
    account_usage = models.IntegerField()
    classification_enum = models.IntegerField()
    description = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'acc_gl_account'

class AccGlClosure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    office = models.ForeignKey('MOffice',related_name="closure_offices")
    closing_date = models.DateField(unique=True)
    is_deleted = models.IntegerField()
    createdby = models.ForeignKey('MAppuser',related_name="clojure_creators", null=True, blank=True)
    lastmodifiedby = models.ForeignKey('MAppuser',related_name="modifiers", null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    comments = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'acc_gl_closure'

class AccGlJournalEntry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    account = models.ForeignKey(AccGlAccount)
    office = models.ForeignKey('MOffice',related_name="journal_offices")
    reversal = models.ForeignKey('self', null=True, blank=True)
    transaction_id = models.CharField(max_length=150)
    reversed = models.IntegerField()
    manual_entry = models.IntegerField()
    entry_date = models.DateField()
    type_enum = models.IntegerField()
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    description = models.CharField(max_length=1500, blank=True)
    entity_type_enum = models.IntegerField(null=True, blank=True)
    entity_id = models.BigIntegerField(null=True, blank=True)
    createdby = models.ForeignKey('MAppuser',related_name="creators")
    lastmodifiedby = models.ForeignKey('MAppuser')
    created_date = models.DateTimeField()
    lastmodified_date = models.DateTimeField()
    class Meta:
        db_table = u'acc_gl_journal_entry'

class AccProductMapping(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gl_account_id = models.BigIntegerField(null=True, blank=True)
    product_id = models.BigIntegerField(null=True, blank=True)
    product_type = models.IntegerField(null=True, blank=True)
    financial_account_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'acc_product_mapping'

class CConfiguration(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    enabled = models.IntegerField()
    class Meta:
        db_table = u'c_configuration'

class ClientAdditionalData(models.Model):
    client = models.ForeignKey('MClient', primary_key=True)
    gender_cd = models.IntegerField(db_column='Gender_cd') # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date of Birth') # Field renamed to remove spaces. Field name made lowercase.
    home_address = models.TextField(db_column='Home address') # Field renamed to remove spaces. Field name made lowercase.
    telephone_number = models.CharField(max_length=60, db_column='Telephone number') # Field renamed to remove spaces. Field name made lowercase.
    telephone_number_2 = models.CharField(max_length=60, db_column='Telephone number (2nd)') # Field renamed to remove spaces. Field name made lowercase.
    email_address = models.CharField(max_length=150, db_column='Email address') # Field renamed to remove spaces. Field name made lowercase.
    educationlevel_cd = models.IntegerField(db_column='EducationLevel_cd') # Field name made lowercase.
    maritalstatus_cd = models.IntegerField(db_column='MaritalStatus_cd') # Field name made lowercase.
    number_of_children = models.IntegerField(db_column='Number of children') # Field renamed to remove spaces. Field name made lowercase.
    citizenship = models.CharField(max_length=150, db_column='Citizenship') # Field name made lowercase.
    povertystatus_cd = models.IntegerField(db_column='PovertyStatus_cd') # Field name made lowercase.
    yesno_cd_employed = models.IntegerField(db_column='YesNo_cd_Employed') # Field name made lowercase.
    fieldofemployment_cd_field_of_employment = models.IntegerField(null=True, db_column='FieldOfEmployment_cd_Field of employment', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    employer_name = models.CharField(max_length=150, db_column='Employer name', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    number_of_years = models.IntegerField(null=True, db_column='Number of years', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    monthly_salary = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Monthly salary', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_self_employed = models.IntegerField(db_column='YesNo_cd_Self employed') # Field renamed to remove spaces. Field name made lowercase.
    fieldofemployment_cd_field_of_self_employment = models.IntegerField(null=True, db_column='FieldOfEmployment_cd_Field of self-employment', blank=True) # Field renamed to remove spaces. Field renamed to remove dashes. Field name made lowercase.
    business_address = models.TextField(db_column='Business address', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    number_of_employees = models.IntegerField(null=True, db_column='Number of employees', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    monthly_salaries_paid = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Monthly salaries paid', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    monthly_net_income_of_business_activity = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Monthly net income of business activity', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    monthly_rent = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Monthly rent', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    other_income_generating_activities = models.CharField(max_length=300, db_column='Other income generating activities', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_bookkeeping = models.IntegerField(null=True, db_column='YesNo_cd_Bookkeeping', blank=True) # Field name made lowercase.
    yesno_cd_loans_with_other_institutions = models.IntegerField(db_column='YesNo_cd_Loans with other institutions') # Field renamed to remove spaces. Field name made lowercase.
    from_whom = models.CharField(max_length=300, db_column='From whom', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    amount = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Amount', blank=True) # Field name made lowercase.
    interest_rate_pa = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Interest rate pa', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    number_of_people_depending_on_overal_income = models.IntegerField(db_column='Number of people depending on overal income') # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_bank_account = models.IntegerField(db_column='YesNo_cd_Bank account') # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_business_plan_provided = models.IntegerField(db_column='YesNo_cd_Business plan provided') # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_access_to_internet = models.IntegerField(null=True, db_column='YesNo_cd_Access to internet', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    introduced_by = models.CharField(max_length=300, db_column='Introduced by', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    known_to_introducer_since = models.CharField(max_length=300, db_column='Known to introducer since') # Field renamed to remove spaces. Field name made lowercase.
    last_visited_by = models.CharField(max_length=300, db_column='Last visited by', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    last_visited_on = models.DateField(db_column='Last visited on') # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'client additional data'

class ExtraClientDetails(models.Model):
    client = models.ForeignKey('MClient', primary_key=True)
    business_description = models.CharField(max_length=300, db_column='Business Description', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    years_in_business = models.IntegerField(null=True, db_column='Years in Business', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    gender_cd = models.IntegerField(null=True, db_column='Gender_cd', blank=True) # Field name made lowercase.
    education_cv = models.CharField(max_length=180, db_column='Education_cv', blank=True) # Field name made lowercase.
    next_visit = models.DateField(null=True, db_column='Next Visit', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    highest_rate_paid = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Highest Rate Paid', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'extra_client_details'

class ExtraFamilyDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    client = models.ForeignKey('MClient')
    name = models.CharField(max_length=120, db_column='Name', blank=True) # Field name made lowercase.
    date_of_birth = models.DateField(null=True, db_column='Date of Birth', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    points_score = models.IntegerField(null=True, db_column='Points Score', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    education_cd_highest = models.IntegerField(null=True, db_column='Education_cd_Highest', blank=True) # Field name made lowercase.
    other_notes = models.TextField(db_column='Other Notes', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'extra_family_details'

class ExtraLoanDetails(models.Model):
    loan = models.ForeignKey('MLoan', primary_key=True)
    business_description = models.CharField(max_length=300, db_column='Business Description', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    years_in_business = models.IntegerField(null=True, db_column='Years in Business', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    gender_cd = models.IntegerField(null=True, db_column='Gender_cd', blank=True) # Field name made lowercase.
    education_cv = models.CharField(max_length=180, db_column='Education_cv', blank=True) # Field name made lowercase.
    next_visit = models.DateField(null=True, db_column='Next Visit', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    highest_rate_paid = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Highest Rate Paid', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'extra_loan_details'

class ImpactMeasurement(models.Model):
    loan = models.ForeignKey('MLoan', primary_key=True)
    yesno_cd_repaidonschedule = models.IntegerField(db_column='YesNo_cd_RepaidOnSchedule') # Field name made lowercase.
    reasonnotrepaidonschedule = models.TextField(db_column='ReasonNotRepaidOnSchedule', blank=True) # Field name made lowercase.
    how_was_loan_amount_invested = models.TextField(db_column='How was Loan Amount Invested') # Field renamed to remove spaces. Field name made lowercase.
    additional_income_generated = models.DecimalField(decimal_places=6, max_digits=21, db_column='Additional Income Generated') # Field renamed to remove spaces. Field name made lowercase.
    additional_income_used_for = models.TextField(db_column='Additional Income Used For') # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_newjobscreated = models.IntegerField(db_column='YesNo_cd_NewJobsCreated') # Field name made lowercase.
    number_of_jobs_created = models.BigIntegerField(null=True, db_column='Number of Jobs Created', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'impact measurement'

class LatamExtraClientDetails(models.Model):
    client = models.ForeignKey('MClient', primary_key=True)
    business_description = models.CharField(max_length=300, db_column='Business Description', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    years_in_business = models.IntegerField(null=True, db_column='Years in Business', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    gender_cd = models.IntegerField(null=True, db_column='Gender_cd', blank=True) # Field name made lowercase.
    education_cv = models.CharField(max_length=180, db_column='Education_cv', blank=True) # Field name made lowercase.
    next_visit = models.DateField(null=True, db_column='Next Visit', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    highest_rate_paid = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Highest Rate Paid', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'latam_extra_client_details'

class LatamExtraLoanDetails(models.Model):
    loan = models.ForeignKey('MLoan', primary_key=True)
    business_description = models.CharField(max_length=300, db_column='Business Description', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    years_in_business = models.IntegerField(null=True, db_column='Years in Business', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    gender_cd = models.IntegerField(null=True, db_column='Gender_cd', blank=True) # Field name made lowercase.
    education_cv = models.CharField(max_length=180, db_column='Education_cv', blank=True) # Field name made lowercase.
    next_visit = models.DateField(null=True, db_column='Next Visit', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    highest_rate_paid = models.DecimalField(decimal_places=6, null=True, max_digits=21, db_column='Highest Rate Paid', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'latam_extra_loan_details'

class LatamFamilyDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    client = models.ForeignKey('MClient')
    name = models.CharField(max_length=120, db_column='Name', blank=True) # Field name made lowercase.
    date_of_birth = models.DateField(null=True, db_column='Date of Birth', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    points_score = models.IntegerField(null=True, db_column='Points Score', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    education_cd_highest = models.IntegerField(null=True, db_column='Education_cd_Highest', blank=True) # Field name made lowercase.
    other_notes = models.TextField(db_column='Other Notes', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'latam_family_details'

class LoanAdditionalData(models.Model):
    loan = models.ForeignKey('MLoan', primary_key=True)
    purposeofloan_cd = models.IntegerField(db_column='PurposeOfLoan_cd') # Field name made lowercase.
    collateraltype_cd = models.IntegerField(db_column='CollateralType_cd') # Field name made lowercase.
    collateral_notes = models.TextField(db_column='Collateral notes') # Field renamed to remove spaces. Field name made lowercase.
    yesno_cd_guarantor = models.IntegerField(db_column='YesNo_cd_Guarantor') # Field name made lowercase.
    guarantor_name = models.CharField(max_length=250, db_column='Guarantor name', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    guarantor_relation = models.CharField(max_length=300, db_column='Guarantor relation', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    guarantor_address = models.CharField(max_length=300, db_column='Guarantor address', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    guarantor_telephone_number = models.CharField(max_length=60, db_column='Guarantor telephone number', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'loan additional data'

class MAppuser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    is_deleted = models.IntegerField()
    office = models.ForeignKey('MOffice', related_name="user_offices", null=True, blank=True)
    username = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    password = models.CharField(max_length=765)
    email = models.CharField(max_length=300)
    firsttime_login_remaining = models.TextField() # This field type is a guess.
    nonexpired = models.TextField() # This field type is a guess.
    nonlocked = models.TextField() # This field type is a guess.
    nonexpired_credentials = models.TextField() # This field type is a guess.
    enabled = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'm_appuser'

class MAppuserRole(models.Model):
    appuser = models.ForeignKey(MAppuser)
    role = models.ForeignKey('MRole')
    class Meta:
        db_table = u'm_appuser_role'

class MCalendar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    entity_id = models.BigIntegerField()
    entity_type_enum = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    calendar_type_enum = models.IntegerField()
    repeating = models.IntegerField()
    recurrence = models.CharField(max_length=300)
    remind_by_enum = models.IntegerField(null=True, blank=True)
    first_reminder = models.IntegerField()
    second_reminder = models.IntegerField()
    class Meta:
        db_table = u'm_calendar'

class MCharge(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True, blank=True)
    currency_code = models.CharField(max_length=9)
    charge_applies_to_enum = models.IntegerField()
    charge_time_enum = models.IntegerField()
    charge_calculation_enum = models.IntegerField()
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    is_penalty = models.IntegerField()
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    class Meta:
        db_table = u'm_charge'

class MClient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    account_no = models.CharField(max_length=60, unique=True)
    office = models.ForeignKey('MOffice',related_name="client_offices")
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    middlename = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    fullname = models.CharField(max_length=300, blank=True)
    display_name = models.CharField(max_length=300)
    image_key = models.CharField(max_length=1500, blank=True)
    #joined_date = models.DateField(null=True, blank=True)
    #is_deleted = models.IntegerField()
    def __str__(self):
        return "%s(%s)"%(self.display_name,str(self.external_id))
    class Meta:
        db_table = u'm_client'

class MClientIdentifier(models.Model):
    id = models.BigIntegerField(primary_key=True)
    client = models.ForeignKey(MClient)
    document_type = models.ForeignKey('MCodeValue')
    document_key = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=1500, blank=True)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'm_client_identifier'

class MCode(models.Model):
    id = models.IntegerField(primary_key=True)
    code_name = models.CharField(max_length=200, unique=True, blank=True)
    is_system_defined = models.IntegerField()
    class Meta:
        db_table = u'm_code'

class MCodeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.ForeignKey(MCode)
    code_value = models.CharField(max_length=200, unique=True, blank=True)
    order_position = models.IntegerField()
    class Meta:
        db_table = u'm_code_value'

class MCurrency(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=9, unique=True)
    decimal_places = models.IntegerField()
    display_symbol = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=150)
    internationalized_name_code = models.CharField(max_length=150)
    class Meta:
        db_table = u'm_currency'

class MDepositAccount(models.Model):
    id = models.BigIntegerField(primary_key=True)
    is_deleted = models.IntegerField()
    status_enum = models.IntegerField()
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    client = models.ForeignKey(MClient)
    product = models.ForeignKey('MProductDeposit')
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    deposit_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    maturity_nominal_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    tenure_months = models.IntegerField()
    interest_compounded_every = models.IntegerField()
    interest_compounded_every_period_enum = models.IntegerField()
    projected_commencement_date = models.DateField()
    actual_commencement_date = models.DateField(null=True, blank=True)
    matures_on_date = models.DateTimeField(null=True, blank=True)
    projected_interest_accrued_on_maturity = models.DecimalField(max_digits=21, decimal_places=6)
    actual_interest_accrued = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    projected_total_maturity_amount = models.DecimalField(max_digits=21, decimal_places=6)
    actual_total_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    is_compounding_interest_allowed = models.IntegerField()
    interest_paid = models.DecimalField(max_digits=21, decimal_places=6)
    is_interest_withdrawable = models.IntegerField()
    available_interest = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    interest_posted_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    last_interest_posted_date = models.DateField(null=True, blank=True)
    next_interest_posting_date = models.DateField(null=True, blank=True)
    is_renewal_allowed = models.IntegerField()
    renewed_account = models.ForeignKey('self', null=True, blank=True)
    is_preclosure_allowed = models.IntegerField()
    pre_closure_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    is_lock_in_period_allowed = models.IntegerField()
    lock_in_period = models.BigIntegerField(null=True, blank=True)
    lock_in_period_type = models.IntegerField()
    withdrawnon_date = models.DateTimeField(null=True, blank=True)
    rejectedon_date = models.DateTimeField(null=True, blank=True)
    closedon_date = models.DateTimeField(null=True, blank=True)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_deposit_account'

class MDepositAccountTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    deposit_account = models.ForeignKey(MDepositAccount)
    transaction_type_enum = models.IntegerField()
    contra = models.ForeignKey('self', null=True, blank=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    interest = models.DecimalField(max_digits=21, decimal_places=6)
    total = models.DecimalField(max_digits=21, decimal_places=6)
    class Meta:
        db_table = u'm_deposit_account_transaction'

class MDocument(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_entity_type = models.CharField(max_length=150)
    parent_entity_id = models.IntegerField()
    name = models.CharField(max_length=200)
    file_name = models.CharField(max_length=750)
    size = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=3000, blank=True)
    location = models.CharField(max_length=1500)
    class Meta:
        db_table = u'm_document'

class MFund(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=250, unique=True, blank=True)
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    class Meta:
        db_table = u'm_fund'

class MGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    office = models.ForeignKey('MOffice',related_name="group_offices")
    staff = models.ForeignKey('MStaff', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    level = models.ForeignKey('MGroupLevel', db_column='level_Id') # Field name made lowercase.
    hierarchy = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=200, unique=True, blank=True)
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    is_deleted = models.IntegerField()
    class Meta:
        db_table = u'm_group'

class MGroupClient(models.Model):
    group = models.ForeignKey(MGroup, primary_key=True)
    client = models.ForeignKey(MClient)
    class Meta:
        db_table = u'm_group_client'

class MGroupLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    super_parent = models.IntegerField()
    level_name = models.CharField(max_length=300)
    recursable = models.IntegerField()
    can_have_clients = models.IntegerField()
    class Meta:
        db_table = u'm_group_level'

class MGuarantor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey('MLoan')
    type_enum = models.IntegerField()
    entity_id = models.BigIntegerField(null=True, blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    dob = models.DateField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=1500, blank=True)
    address_line_2 = models.CharField(max_length=1500, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    zip = models.CharField(max_length=60, blank=True)
    house_phone_number = models.CharField(max_length=60, blank=True)
    mobile_number = models.CharField(max_length=60, blank=True)
    comment = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'm_guarantor'

class MLoan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    account_no = models.CharField(max_length=60, unique=True)
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    client = models.ForeignKey(MClient, null=True, blank=True)
    group = models.ForeignKey(MGroup, null=True, blank=True)
    product = models.ForeignKey('MProductLoan', null=True, blank=True)
    fund = models.ForeignKey(MFund, null=True, blank=True)
    loan_officer = models.ForeignKey('MStaff', null=True, blank=True)
    loanpurpose_cv = models.ForeignKey(MCodeValue, null=True, blank=True)
    loan_status_id = models.IntegerField()
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    principal_amount = models.DecimalField(max_digits=21, decimal_places=6)
    arrearstolerance_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    nominal_interest_rate_per_period = models.DecimalField(max_digits=21, decimal_places=6)
    interest_period_frequency_enum = models.IntegerField()
    annual_nominal_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    interest_method_enum = models.IntegerField()
    interest_calculated_in_period_enum = models.IntegerField()
    term_frequency = models.IntegerField()
    term_period_frequency_enum = models.IntegerField()
    repay_every = models.IntegerField()
    repayment_period_frequency_enum = models.IntegerField()
    number_of_repayments = models.IntegerField()
    amortization_method_enum = models.IntegerField()
    submittedon_date = models.DateField(null=True, blank=True)
    submittedon_userid = models.ForeignKey(MAppuser, null=True, related_name='submittedon_user' , db_column='submittedon_userid', blank=True)
    approvedon_date = models.DateField(null=True, blank=True)
    approvedon_userid = models.ForeignKey(MAppuser, null=True, db_column='approvedon_userid',related_name="mlapprovedon_user", blank=True)
    expected_disbursedon_date = models.DateField(null=True, blank=True)
    expected_firstrepaymenton_date = models.DateField(null=True, blank=True)
    interest_calculated_from_date = models.DateField(null=True, blank=True)
    disbursedon_date = models.DateField(null=True, blank=True)
    disbursedon_userid = models.ForeignKey(MAppuser, null=True,related_name='disburseuser', db_column='disbursedon_userid', blank=True)
    expected_maturedon_date = models.DateField(null=True, blank=True)
    maturedon_date = models.DateField(null=True, blank=True)
    closedon_date = models.DateField(null=True, blank=True)
    closedon_userid = models.ForeignKey(MAppuser, related_name="closedon_users",null=True, db_column='closedon_userid', blank=True)
    total_charges_due_at_disbursement_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    principal_disbursed_derived = models.DecimalField(max_digits=21, decimal_places=6)
    principal_repaid_derived = models.DecimalField(max_digits=21, decimal_places=6)
    principal_writtenoff_derived = models.DecimalField(max_digits=21, decimal_places=6)
    principal_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_charged_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_repaid_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_waived_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_writtenoff_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_charged_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_repaid_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_waived_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_writtenoff_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_charged_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_repaid_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_waived_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_writtenoff_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_expected_repayment_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_repayment_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_expected_costofloan_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_costofloan_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_waived_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_writtenoff_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    rejectedon_date = models.DateField(null=True, blank=True)
    rejectedon_userid = models.ForeignKey(MAppuser, null=True, related_name="rejectedusers_on" ,db_column='rejectedon_userid', blank=True)
    rescheduledon_date = models.DateField(null=True, blank=True)
    withdrawnon_date = models.DateField(null=True, blank=True)
    withdrawnon_userid = models.ForeignKey(MAppuser, null=True, related_name="withdrawon_users", db_column='withdrawnon_userid', blank=True)
    writtenoffon_date = models.DateField(null=True, blank=True)
    loan_transaction_strategy = models.ForeignKey('RefLoanTransactionProcessingStrategy', null=True, blank=True)
    class Meta:
        db_table = u'm_loan'

class MLoanArrearsAging(models.Model):
    loan = models.ForeignKey(MLoan, primary_key=True)
    principal_overdue_derived = models.DecimalField(max_digits=21, decimal_places=6)
    interest_overdue_derived = models.DecimalField(max_digits=21, decimal_places=6)
    fee_charges_overdue_derived = models.DecimalField(max_digits=21, decimal_places=6)
    penalty_charges_overdue_derived = models.DecimalField(max_digits=21, decimal_places=6)
    total_overdue_derived = models.DecimalField(max_digits=21, decimal_places=6)
    overdue_since_date_derived = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'm_loan_arrears_aging'

class MLoanCharge(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey(MLoan)
    charge = models.ForeignKey(MCharge)
    is_penalty = models.IntegerField()
    charge_time_enum = models.IntegerField()
    due_for_collection_as_of_date = models.DateField(null=True, blank=True)
    charge_calculation_enum = models.IntegerField()
    calculation_percentage = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    calculation_on_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    amount_paid_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    amount_waived_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    amount_writtenoff_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    amount_outstanding_derived = models.DecimalField(max_digits=21, decimal_places=6)
    is_paid_derived = models.IntegerField()
    class Meta:
        db_table = u'm_loan_charge'

class MLoanCollateral(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey(MLoan)
    type_cv = models.ForeignKey(MCodeValue)
    description = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'm_loan_collateral'

class MLoanOfficerAssignmentHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey(MLoan)
    loan_officer = models.ForeignKey('MStaff', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_loan_officer_assignment_history'

class MLoanRepaymentSchedule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey(MLoan)
    fromdate = models.DateField(null=True, blank=True)
    duedate = models.DateField()
    installment = models.IntegerField()
    principal_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    principal_completed_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    principal_writtenoff_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    interest_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    interest_completed_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    interest_writtenoff_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    fee_charges_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    fee_charges_completed_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    fee_charges_writtenoff_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    fee_charges_waived_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    penalty_charges_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    penalty_charges_completed_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    penalty_charges_writtenoff_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    penalty_charges_waived_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    completed_derived = models.TextField() # This field type is a guess.
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    interest_waived_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    class Meta:
        db_table = u'm_loan_repayment_schedule'

class MLoanTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    loan = models.ForeignKey(MLoan)
    is_reversed = models.IntegerField()
    transaction_type_enum = models.IntegerField()
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    principal_portion_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    interest_portion_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    fee_charges_portion_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    penalty_charges_portion_derived = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    class Meta:
        db_table = u'm_loan_transaction'

class MNote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    client = models.ForeignKey(MClient, null=True, blank=True)
    group = models.ForeignKey(MGroup, null=True, blank=True)
    loan = models.ForeignKey(MLoan, null=True, blank=True)
    loan_transaction = models.ForeignKey(MLoanTransaction, null=True, blank=True)
    #deposit_account = models.ForeignKey(MDepositAccount, null=True, blank=True)
    saving_account = models.ForeignKey('MSavingAccount', null=True, blank=True)
    note_type_enum = models.IntegerField()
    note = models.CharField(max_length=3000, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    createdby = models.ForeignKey(MAppuser, null=True, related_name="note_creators",blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby = models.ForeignKey(MAppuser, null=True, blank=True)
    class Meta:
        db_table = u'm_note'

class MOffice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    hierarchy = models.CharField(max_length=300, blank=True)
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=150, unique=True)
    opening_date = models.DateField()
    class Meta:
        db_table = u'm_office'

class MOfficeTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    from_office = models.ForeignKey(MOffice, null=True, blank=True,related_name="from_offices")
    to_office = models.ForeignKey(MOffice, null=True, blank=True,related_name="to_offices")
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=21, decimal_places=6)
    transaction_date = models.DateField()
    description = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'm_office_transaction'

class MOrganisationCurrency(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=9)
    decimal_places = models.IntegerField()
    name = models.CharField(max_length=150)
    display_symbol = models.CharField(max_length=30, blank=True)
    internationalized_name_code = models.CharField(max_length=150)
    class Meta:
        db_table = u'm_organisation_currency'

class MPermission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    grouping = models.CharField(max_length=135, blank=True)
    code = models.CharField(max_length=200, unique=True)
    entity_name = models.CharField(max_length=300, blank=True)
    action_name = models.CharField(max_length=300, blank=True)
    can_maker_checker = models.IntegerField()
    class Meta:
        db_table = u'm_permission'

class MPortfolioCommandSource(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action_name = models.CharField(max_length=150)
    entity_name = models.CharField(max_length=150)
    office_id = models.BigIntegerField(null=True, blank=True)
    group_id = models.BigIntegerField(null=True, blank=True)
    client_id = models.BigIntegerField(null=True, blank=True)
    loan_id = models.BigIntegerField(null=True, blank=True)
    api_get_url = models.CharField(max_length=300)
    resource_id = models.BigIntegerField(null=True, blank=True)
    command_as_json = models.TextField()
    maker = models.ForeignKey(MAppuser,related_name="makers")
    made_on_date = models.DateTimeField()
    checker = models.ForeignKey(MAppuser,related_name="checkers", null=True, blank=True)
    checked_on_date = models.DateTimeField(null=True, blank=True)
    processing_result_enum = models.IntegerField()
    class Meta:
        db_table = u'm_portfolio_command_source'

class MProductDeposit(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    is_deleted = models.IntegerField()
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    min_deposit = models.DecimalField(max_digits=21, decimal_places=6)
    max_deposit = models.DecimalField(max_digits=21, decimal_places=6)
    default_deposit = models.DecimalField(max_digits=21, decimal_places=6)
    tenure_months = models.IntegerField()
    interest_compounded_every = models.IntegerField()
    interest_compounded_every_period_enum = models.IntegerField()
    min_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    max_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    default_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    is_compounding_interest_allowed = models.IntegerField()
    is_renewal_allowed = models.IntegerField()
    is_preclosure_allowed = models.IntegerField()
    pre_closure_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    is_lock_in_period_allowed = models.IntegerField()
    lock_in_period = models.BigIntegerField(null=True, blank=True)
    lock_in_period_type = models.IntegerField()
    class Meta:
        db_table = u'm_product_deposit'

class MProductLoan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    principal_amount = models.DecimalField(max_digits=21, decimal_places=6)
    arrearstolerance_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1500, blank=True)
    fund = models.ForeignKey(MFund, null=True, blank=True)
    nominal_interest_rate_per_period = models.DecimalField(max_digits=21, decimal_places=6)
    interest_period_frequency_enum = models.IntegerField()
    annual_nominal_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    interest_method_enum = models.IntegerField()
    interest_calculated_in_period_enum = models.IntegerField()
    repay_every = models.IntegerField()
    repayment_period_frequency_enum = models.IntegerField()
    number_of_repayments = models.IntegerField()
    amortization_method_enum = models.IntegerField()
    accounting_type = models.IntegerField()
    loan_transaction_strategy = models.ForeignKey('RefLoanTransactionProcessingStrategy', null=True, blank=True)
    class Meta:
        db_table = u'm_product_loan'

class MProductLoanCharge(models.Model):
    product_loan = models.ForeignKey(MProductLoan, primary_key=True)
    charge = models.ForeignKey(MCharge)
    class Meta:
        db_table = u'm_product_loan_charge'

class MProductSavings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True)
    currency_code = models.CharField(max_length=9, blank=True)
    currency_digits = models.IntegerField(null=True, blank=True)
    interest_rate = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    min_interest_rate = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    max_interest_rate = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    savings_deposit_amount = models.DecimalField(max_digits=21, decimal_places=6)
    savings_product_type = models.IntegerField(null=True, blank=True)
    tenure_type = models.IntegerField(null=True, blank=True)
    deposit_every = models.BigIntegerField(null=True, blank=True)
    tenure = models.IntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    interest_type = models.IntegerField(null=True, blank=True)
    interest_calculation_method = models.IntegerField(null=True, blank=True)
    min_bal_for_withdrawal = models.DecimalField(max_digits=21, decimal_places=6)
    is_partial_deposit_allowed = models.IntegerField()
    is_lock_in_period_allowed = models.IntegerField()
    lock_in_period = models.BigIntegerField(null=True, blank=True)
    lock_in_period_type = models.IntegerField()
    is_deleted = models.IntegerField()
    createdby = models.ForeignKey(MAppuser,related_name="savings_creators", null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby = models.ForeignKey(MAppuser, null=True, blank=True)
    class Meta:
        db_table = u'm_product_savings'

class MRole(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1500)
    class Meta:
        db_table = u'm_role'

class MRolePermission(models.Model):
    role = models.ForeignKey(MRole)
    permission = models.ForeignKey(MPermission)
    class Meta:
        db_table = u'm_role_permission'

class MSavingAccount(models.Model):
    id = models.BigIntegerField(primary_key=True)
    is_deleted = models.IntegerField()
    status_enum = models.IntegerField()
    external_id = models.CharField(max_length=200, unique=True, blank=True)
    client = models.ForeignKey(MClient)
    product = models.ForeignKey(MProductSavings)
    deposit_amount_per_period = models.DecimalField(max_digits=21, decimal_places=6)
    savings_product_type = models.IntegerField(null=True, blank=True)
    currency_code = models.CharField(max_length=9)
    currency_digits = models.IntegerField()
    total_deposit_amount = models.DecimalField(max_digits=21, decimal_places=6)
    reccuring_nominal_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    regular_saving_nominal_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    tenure = models.IntegerField()
    tenure_type = models.IntegerField(null=True, blank=True)
    deposit_every = models.BigIntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    interest_posting_every = models.IntegerField(null=True, blank=True)
    interest_posting_frequency = models.IntegerField(null=True, blank=True)
    interest_type = models.IntegerField(null=True, blank=True)
    interest_calculation_method = models.IntegerField(null=True, blank=True)
    projected_commencement_date = models.DateField()
    actual_commencement_date = models.DateField(null=True, blank=True)
    matures_on_date = models.DateTimeField(null=True, blank=True)
    projected_interest_accrued_on_maturity = models.DecimalField(max_digits=21, decimal_places=6)
    actual_interest_accrued = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    projected_total_maturity_amount = models.DecimalField(max_digits=21, decimal_places=6)
    actual_total_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    is_preclosure_allowed = models.IntegerField()
    pre_closure_interest_rate = models.DecimalField(max_digits=21, decimal_places=6)
    outstanding_amount = models.DecimalField(max_digits=21, decimal_places=6)
    interest_posted_amount = models.DecimalField(null=True, max_digits=21, decimal_places=6, blank=True)
    last_interest_posted_date = models.DateField(null=True, blank=True)
    next_interest_posting_date = models.DateField(null=True, blank=True)
    is_lock_in_period_allowed = models.IntegerField()
    lock_in_period = models.BigIntegerField(null=True, blank=True)
    lock_in_period_type = models.IntegerField()
    withdrawnon_date = models.DateTimeField(null=True, blank=True)
    rejectedon_date = models.DateTimeField(null=True, blank=True)
    closedon_date = models.DateTimeField(null=True, blank=True)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_saving_account'

class MSavingAccountTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    saving_account = models.ForeignKey(MSavingAccount)
    transaction_type_enum = models.IntegerField()
    contra = models.ForeignKey('self', null=True, blank=True)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=21, decimal_places=6)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_saving_account_transaction'

class MSavingSchedule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    saving_account = models.ForeignKey(MSavingAccount)
    duedate = models.DateField()
    installment = models.IntegerField()
    deposit = models.DecimalField(max_digits=23, decimal_places=4)
    payment_date = models.DateField(null=True, blank=True)
    deposit_paid = models.DecimalField(null=True, max_digits=23, decimal_places=4, blank=True)
    interest_accured = models.DecimalField(null=True, max_digits=23, decimal_places=4, blank=True)
    completed_derived = models.TextField() # This field type is a guess.
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'm_saving_schedule'

class MStaff(models.Model):
    id = models.BigIntegerField(primary_key=True)
    is_loan_officer = models.IntegerField()
    office = models.ForeignKey(MOffice,related_name="staff_offices", null=True, blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    display_name = models.CharField(max_length=200, unique=True)
    class Meta:
        db_table = u'm_staff'

class REnumValue(models.Model):
    enum_name = models.CharField(max_length=200, unique=True)
    enum_id = models.IntegerField(primary_key=True)
    enum_message_property = models.CharField(max_length=200, unique=True)
    enum_value = models.CharField(max_length=200, unique=True)
    class Meta:
        db_table = u'r_enum_value'

class RefLoanTransactionProcessingStrategy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    createdby_id = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    lastmodifiedby_id = models.BigIntegerField(null=True, blank=True)
    lastmodified_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ref_loan_transaction_processing_strategy'

class RptSequence(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'rpt_sequence'

class StretchyParameter(models.Model):
    parameter_id = models.IntegerField(primary_key=True)
    parameter_name = models.CharField(max_length=135, unique=True)
    parameter_variable = models.CharField(max_length=135, blank=True)
    parameter_label = models.CharField(max_length=135)
    parameter_displaytype = models.CharField(max_length=135, db_column='parameter_displayType') # Field name made lowercase.
    parameter_formattype = models.CharField(max_length=30, db_column='parameter_FormatType') # Field name made lowercase.
    parameter_default = models.CharField(max_length=135)
    special = models.CharField(max_length=3, blank=True)
    selectone = models.CharField(max_length=3, db_column='selectOne', blank=True) # Field name made lowercase.
    selectall = models.CharField(max_length=3, db_column='selectAll', blank=True) # Field name made lowercase.
    parameter_sql = models.TextField(blank=True)
    class Meta:
        db_table = u'stretchy_parameter'

class StretchyReport(models.Model):
    report_id = models.IntegerField(primary_key=True)
    report_name = models.CharField(max_length=200, unique=True)
    report_type = models.CharField(max_length=60)
    report_subtype = models.CharField(max_length=60, blank=True)
    report_category = models.CharField(max_length=135, blank=True)
    report_sql = models.TextField(blank=True)
    description = models.TextField(blank=True)
    core_report = models.IntegerField(null=True, blank=True)
    use_report = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'stretchy_report'

class StretchyReportParameter(models.Model):
    report_id = models.IntegerField(unique=True)
    parameter_id = models.IntegerField(primary_key=True)
    report_parameter_name = models.CharField(max_length=135, unique=True, blank=True)
    class Meta:
        db_table = u'stretchy_report_parameter'

class XRegisteredTable(models.Model):
    registered_table_name = models.CharField(max_length=150, primary_key=True)
    application_table_name = models.CharField(max_length=150)
    class Meta:
        db_table = u'x_registered_table'

class MobilePayment(models.Model):
    created=models.DateTimeField(auto_now=True)
    sender=models.CharField(max_length=100)
    approved=models.BooleanField(default=False)
    amount=models.IntegerField(max_length=50)
    client=models.ForeignKey(MClient,related_name="payers",null=True)


