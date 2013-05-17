# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ResUserResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(ResUser, db_column='user')
    group = models.ForeignKey(ResGroup, db_column='group')
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'res_user-res_group'

class IrTranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    lang = models.CharField(max_length=-1)
    src = models.TextField()
    src_md5 = models.CharField(max_length=32)
    name = models.CharField(max_length=-1)
    res_id = models.IntegerField()
    value = models.TextField()
    type = models.CharField(max_length=-1)
    module = models.CharField(max_length=-1)
    fuzzy = models.BooleanField()
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'ir_translation'

class WebdavCollection(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    domain = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    model = models.ForeignKey(IrModel, db_column='model')
    class Meta:
        db_table = u'webdav_collection'

class IrSequenceType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_sequence_type'

class ProductCategoryCustomerTaxesRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(ProductCategory, db_column='category')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    class Meta:
        db_table = u'product_category_customer_taxes_rel'

class PartyContactMechanism(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    comment = models.TextField()
    sequence = models.IntegerField()
    value = models.CharField(max_length=-1)
    active = models.BooleanField()
    party = models.ForeignKey(PartyParty, db_column='party')
    type = models.CharField(max_length=-1)
    class Meta:
        db_table = u'party_contact_mechanism'

class IrModuleModule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(unique=True, max_length=-1)
    state = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_module_module'

class IrModuleModuleDependency(models.Model):
    id = models.IntegerField(primary_key=True)
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    module = models.ForeignKey(IrModuleModule, db_column='module')
    class Meta:
        db_table = u'ir_module_module_dependency'

class WebdavShare(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    expiration_date = models.DateField()
    note = models.TextField()
    user = models.ForeignKey(ResUser, db_column='user')
    key = models.CharField(max_length=-1)
    path = models.CharField(max_length=-1)
    class Meta:
        db_table = u'webdav_share'

class PartyConfiguration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'party_configuration'

class CurrencyCurrency(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=3)
    p_sep_by_space = models.BooleanField()
    active = models.BooleanField()
    mon_grouping = models.CharField(max_length=-1)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    numeric_code = models.CharField(max_length=3)
    n_cs_precedes = models.BooleanField()
    n_sign_posn = models.IntegerField()
    p_cs_precedes = models.BooleanField()
    mon_decimal_point = models.CharField(max_length=-1)
    symbol = models.CharField(max_length=10)
    mon_thousands_sep = models.CharField(max_length=-1)
    negative_sign = models.CharField(max_length=-1)
    n_sep_by_space = models.BooleanField()
    positive_sign = models.CharField(max_length=-1)
    digits = models.IntegerField()
    name = models.CharField(max_length=-1)
    p_sign_posn = models.IntegerField()
    class Meta:
        db_table = u'currency_currency'

class ProductCategorySupplierTaxesRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(ProductCategory, db_column='category')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    class Meta:
        db_table = u'product_category_supplier_taxes_rel'

class CurrencyCurrencyRate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    date = models.DateField()
    class Meta:
        db_table = u'currency_currency_rate'

class IrUiMenu(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', db_column='parent')
    name = models.CharField(max_length=-1)
    icon = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'ir_ui_menu'

class ProductCustomerTaxesRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductTemplate, db_column='product')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    class Meta:
        db_table = u'product_customer_taxes_rel'

class SergerySergery(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'sergery_sergery'

class ProductUomCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'product_uom_category'

class ProductSupplierTaxesRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductTemplate, db_column='product')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    class Meta:
        db_table = u'product_supplier_taxes_rel'

class IrSequence(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    last_timestamp = models.IntegerField()
    number_next_internal = models.IntegerField()
    timestamp_rounding = models.FloatField()
    padding = models.IntegerField()
    number_increment = models.IntegerField()
    prefix = models.CharField(max_length=-1)
    timestamp_offset = models.FloatField()
    active = models.BooleanField()
    type = models.CharField(max_length=-1)
    suffix = models.CharField(max_length=-1)
    company = models.ForeignKey(CompanyCompany, db_column='company')
    class Meta:
        db_table = u'ir_sequence'

class ResUserCompanyEmployee(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser, db_column='user')
    employee = models.ForeignKey(CompanyEmployee, db_column='employee')
    class Meta:
        db_table = u'res_user-company_employee'

class IrUiViewSc(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    user = models.ForeignKey(ResUser)
    resource = models.CharField(max_length=-1)
    res_id = models.IntegerField()
    class Meta:
        db_table = u'ir_ui_view_sc'

class CompanyEmployee(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    party = models.ForeignKey(PartyParty, db_column='party')
    class Meta:
        db_table = u'company_employee'

class IrUiViewTreeWidth(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    width = models.IntegerField()
    field = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUser, db_column='user')
    model = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_ui_view_tree_width'

class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    taxes_parent = models.BooleanField()
    account_parent = models.BooleanField()
    class Meta:
        db_table = u'product_category'

class ProductUom(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(ProductUomCategory, db_column='category')
    digits = models.IntegerField()
    name = models.CharField(max_length=-1)
    rounding = models.FloatField()
    symbol = models.CharField(max_length=10)
    rate = models.FloatField()
    factor = models.FloatField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_uom'

class IrUiViewTreeExpandedState(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    domain = models.CharField(max_length=-1)
    child_name = models.CharField(max_length=-1)
    nodes = models.TextField()
    user = models.ForeignKey(ResUser, db_column='user')
    model = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_ui_view_tree_expanded_state'

class CronCompanyRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    cron = models.ForeignKey(IrCron, db_column='cron')
    class Meta:
        db_table = u'cron_company_rel'

class GnuhealthNeonatalApgar(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    apgar_score = models.IntegerField()
    apgar_grimace = models.CharField(max_length=-1)
    apgar_minute = models.IntegerField()
    name = models.ForeignKey(GnuhealthNewborn, db_column='name')
    apgar_appearance = models.CharField(max_length=-1)
    apgar_pulse = models.CharField(max_length=-1)
    apgar_activity = models.CharField(max_length=-1)
    apgar_respiration = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_neonatal_apgar'

class ProductTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(ProductCategory, db_column='category')
    name = models.CharField(max_length=-1)
    default_uom = models.ForeignKey(ProductUom, db_column='default_uom')
    active = models.BooleanField()
    consumable = models.BooleanField()
    type = models.CharField(max_length=-1)
    taxes_category = models.BooleanField()
    account_category = models.BooleanField()
    class Meta:
        db_table = u'product_template'

class GnuhealthNewborn(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    reanimation_mask = models.BooleanField()
    photo = models.TextField() # This field type is a guess.
    neonatal_grasp_reflex = models.BooleanField()
    neonatal_blink_reflex = models.BooleanField()
    neonatal_erbs_palsy = models.BooleanField()
    neonatal_barlow = models.BooleanField()
    reanimation_aspiration = models.BooleanField()
    neonatal_sucking_reflex = models.BooleanField()
    cephalic_perimeter = models.IntegerField()
    neonatal_ambiguous_genitalia = models.BooleanField()
    reanimation_stimulation = models.BooleanField()
    neonatal_moro_reflex = models.BooleanField()
    weight = models.IntegerField()
    neonatal_tonic_neck_reflex = models.BooleanField()
    responsible = models.ForeignKey(GnuhealthPhysician, db_column='responsible')
    dismissed = models.DateTimeField()
    neonatal_hernia = models.BooleanField()
    test_toxo = models.BooleanField()
    reanimation_intubation = models.BooleanField()
    neonatal_talipes_equinovarus = models.BooleanField()
    neonatal_rooting_reflex = models.BooleanField()
    neonatal_swimming_reflex = models.BooleanField()
    neonatal_syndactyly = models.BooleanField()
    bd = models.BooleanField()
    test_vdrl = models.BooleanField()
    neonatal_babinski_reflex = models.BooleanField()
    tod = models.DateTimeField()
    died_at_the_hospital = models.BooleanField()
    neonatal_stepping_reflex = models.BooleanField()
    neonatal_ortolani = models.BooleanField()
    meconium = models.BooleanField()
    newborn_name = models.CharField(max_length=-1)
    test_billirubin = models.BooleanField()
    sex = models.CharField(max_length=-1)
    test_chagas = models.BooleanField()
    reanimation_oxygen = models.BooleanField()
    name = models.CharField(unique=True, max_length=-1)
    neonatal_polydactyly = models.BooleanField()
    notes = models.TextField()
    test_audition = models.BooleanField()
    neonatal_hematoma = models.BooleanField()
    test_metabolic = models.BooleanField()
    died_at_delivery = models.BooleanField()
    length = models.IntegerField()
    died_being_transferred = models.BooleanField()
    cod = models.ForeignKey(GnuhealthPathology, db_column='cod')
    neonatal_palmar_crease = models.BooleanField()
    mother = models.ForeignKey(GnuhealthPatient, db_column='mother')
    birth_date = models.DateTimeField()
    apgar5 = models.IntegerField()
    apgar1 = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_newborn'

class CountryCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'country_country'

class CountrySubdivision(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    country = models.ForeignKey(CountryCountry, db_column='country')
    type = models.CharField(max_length=-1)
    class Meta:
        db_table = u'country_subdivision'

class IrProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    res = models.CharField(max_length=-1)
    value = models.CharField(max_length=-1)
    field = models.ForeignKey(IrModelField, db_column='field')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    class Meta:
        db_table = u'ir_property'

class IrUiIcon(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    module = models.CharField(max_length=-1)
    path = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_ui_icon'

class IrActionKeyword(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    keyword = models.CharField(max_length=-1)
    action = models.ForeignKey(IrAction, db_column='action')
    model = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_action_keyword'

class GnuhealthDietBelief(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(unique=True, max_length=-1)
    description = models.TextField()
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_diet_belief'

class IrActionReport(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    direct_print = models.BooleanField()
    extension = models.CharField(max_length=-1)
    template_extension = models.CharField(max_length=-1)
    module = models.CharField(max_length=-1)
    report = models.CharField(max_length=-1)
    report_name = models.CharField(max_length=-1)
    action = models.ForeignKey(IrAction, db_column='action')
    model = models.CharField(max_length=-1)
    report_content_custom = models.TextField() # This field type is a guess.
    email = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_action_report'

class GnuhealthOccupation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(unique=True, max_length=-1)
    class Meta:
        db_table = u'gnuhealth_occupation'

class CalendarCalendarReadResUser(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser, db_column='user')
    calendar = models.ForeignKey(CalendarCalendar, db_column='calendar')
    class Meta:
        db_table = u'calendar_calendar-read-res_user'

class CalendarCalendarWriteResUser(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser, db_column='user')
    calendar = models.ForeignKey(CalendarCalendar, db_column='calendar')
    class Meta:
        db_table = u'calendar_calendar-write-res_user'

class GnuhealthBedTransfer(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    bed_from = models.ForeignKey(GnuhealthHospitalBed, db_column='bed_from')
    reason = models.CharField(max_length=-1)
    transfer_date = models.DateTimeField()
    bed_to = models.ForeignKey(GnuhealthHospitalBed, db_column='bed_to')
    class Meta:
        db_table = u'gnuhealth_bed_transfer'

class GnuhealthPatientPsc(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    psc_takes_unnecesary_risks = models.CharField(max_length=-1)
    psc_fidgety = models.CharField(max_length=-1)
    psc_trouble_sleeping = models.CharField(max_length=-1)
    psc_less_interested_in_friends = models.CharField(max_length=-1)
    psc_trouble_concentrating = models.CharField(max_length=-1)
    psc_daydreams_too_much = models.CharField(max_length=-1)
    psc_visit_doctor_finds_ok = models.CharField(max_length=-1)
    psc_irritable_angry = models.CharField(max_length=-1)
    psc_refuses_to_share = models.CharField(max_length=-1)
    psc_does_not_listen_to_rules = models.CharField(max_length=-1)
    evaluation_start = models.DateTimeField()
    psc_feels_is_bad_child = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUser)
    psc_takes_things_from_others = models.CharField(max_length=-1)
    psc_sad_unhappy = models.CharField(max_length=-1)
    psc_act_as_younger = models.CharField(max_length=-1)
    psc_spend_time_alone = models.CharField(max_length=-1)
    evaluation_date = models.ForeignKey(GnuhealthAppointment, db_column='evaluation_date')
    psc_distracted_easily = models.CharField(max_length=-1)
    psc_total = models.IntegerField()
    psc_school_grades_dropping = models.CharField(max_length=-1)
    psc_having_less_fun = models.CharField(max_length=-1)
    psc_less_interest_in_school = models.CharField(max_length=-1)
    psc_wants_to_be_with_parents = models.CharField(max_length=-1)
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    psc_absent_from_school = models.CharField(max_length=-1)
    psc_worries_a_lot = models.CharField(max_length=-1)
    psc_down_on_self = models.CharField(max_length=-1)
    psc_blames_others = models.CharField(max_length=-1)
    psc_does_not_show_feelings = models.CharField(max_length=-1)
    psc_teases_others = models.CharField(max_length=-1)
    psc_afraid_of_new_situations = models.CharField(max_length=-1)
    psc_does_not_get_people_feelings = models.CharField(max_length=-1)
    psc_feels_hopeless = models.CharField(max_length=-1)
    psc_acts_as_driven_by_motor = models.CharField(max_length=-1)
    psc_aches_pains = models.CharField(max_length=-1)
    notes = models.TextField()
    psc_gets_hurt_often = models.CharField(max_length=-1)
    psc_fights_with_others = models.CharField(max_length=-1)
    psc_trouble_with_teacher = models.CharField(max_length=-1)
    psc_tires_easily = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_patient_psc'

class IrActionActWindow(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    domain = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1)
    auto_refresh = models.IntegerField()
    search_value = models.CharField(max_length=-1)
    window_name = models.BooleanField()
    action = models.ForeignKey(IrAction, db_column='action')
    limit = models.IntegerField()
    context = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_action_act_window'

class IrUiView(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    data = models.TextField()
    field_childs = models.CharField(max_length=-1)
    priority = models.IntegerField()
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    domain = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    inherit = models.ForeignKey('self', db_column='inherit')
    module = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_ui_view'

class IrActionActWindowView(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    act_window = models.ForeignKey(IrActionActWindow, db_column='act_window')
    view = models.ForeignKey(IrUiView, db_column='view')
    class Meta:
        db_table = u'ir_action_act_window_view'

class IrActionWizard(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    wiz_name = models.CharField(max_length=-1)
    window = models.BooleanField()
    action = models.ForeignKey(IrAction, db_column='action')
    model = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_action_wizard'

class IrActionUrl(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    url = models.CharField(max_length=-1)
    action = models.ForeignKey(IrAction, db_column='action')
    class Meta:
        db_table = u'ir_action_url'

class CalendarLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'calendar_location'

class StockLot(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    number = models.CharField(max_length=-1)
    expiration_date = models.DateField()
    class Meta:
        db_table = u'stock_lot'

class CalendarCalendar(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    owner = models.ForeignKey(ResUser, db_column='owner')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'calendar_calendar'

class CalendarCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'calendar_category'

class CalendarEventCalendarCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(CalendarCategory, db_column='category')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    class Meta:
        db_table = u'calendar_event-calendar_category'

class IrModelAccess(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    perm_read = models.BooleanField()
    perm_create = models.BooleanField()
    perm_write = models.BooleanField()
    group = models.ForeignKey(ResGroup, db_column='group')
    model = models.ForeignKey(IrModel, db_column='model')
    perm_delete = models.BooleanField()
    class Meta:
        db_table = u'ir_model_access'

class StockLotType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'stock_lot_type'

class ProductTemplateStockLotType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    template = models.ForeignKey(ProductTemplate, db_column='template')
    type = models.ForeignKey(StockLotType, db_column='type')
    class Meta:
        db_table = u'product_template-stock_lot_type'

class GnuhealthOperationalArea(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    name = models.CharField(unique=True, max_length=-1)
    class Meta:
        db_table = u'gnuhealth_operational_area'

class GnuhealthInpatientMedicationAdminTime(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    admin_time = models.TimeField()
    name = models.ForeignKey(GnuhealthInpatientMedication, db_column='name')
    dose = models.FloatField()
    dose_unit = models.ForeignKey(GnuhealthDoseUnit, db_column='dose_unit')
    remarks = models.TextField()
    class Meta:
        db_table = u'gnuhealth_inpatient_medication_admin_time'

class ResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'res_group'

class IrModelFieldAccess(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    field = models.ForeignKey(IrModelField, db_column='field')
    perm_read = models.BooleanField()
    perm_write = models.BooleanField()
    group = models.ForeignKey(ResGroup, db_column='group')
    perm_create = models.BooleanField()
    perm_delete = models.BooleanField()
    class Meta:
        db_table = u'ir_model_field_access'

class CalendarAlarm(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    valarm = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'calendar_alarm'

class GnuhealthInpatientMedication(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    start_treatment = models.DateTimeField()
    adverse_reaction = models.TextField()
    end_treatment = models.DateTimeField()
    course_completed = models.BooleanField()
    frequency_prn = models.BooleanField()
    frequency = models.IntegerField()
    qty = models.IntegerField()
    common_dosage = models.ForeignKey(GnuhealthMedicationDosage, db_column='common_dosage')
    form = models.ForeignKey(GnuhealthDrugForm, db_column='form')
    is_active = models.BooleanField()
    medicament = models.ForeignKey(GnuhealthMedicament, db_column='medicament')
    dose = models.FloatField()
    dose_unit = models.ForeignKey(GnuhealthDoseUnit, db_column='dose_unit')
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    route = models.ForeignKey(GnuhealthDrugRoute, db_column='route')
    frequency_unit = models.CharField(max_length=-1)
    indication = models.ForeignKey(GnuhealthPathology, db_column='indication')
    discontinued_reason = models.CharField(max_length=-1)
    discontinued = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_inpatient_medication'

class CalendarEventAlarm(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    calendar_alarm = models.ForeignKey(CalendarAlarm, db_column='calendar_alarm')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    class Meta:
        db_table = u'calendar_event_alarm'

class IrModelButton(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    model = models.ForeignKey(IrModel, db_column='model')
    class Meta:
        db_table = u'ir_model_button'

class GnuhealthOperationalSector(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    name = models.CharField(max_length=-1)
    operational_area = models.ForeignKey(GnuhealthOperationalArea, db_column='operational_area')
    class Meta:
        db_table = u'gnuhealth_operational_sector'

class GnuhealthInpatientMedicationLog(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    admin_time = models.DateTimeField()
    name = models.ForeignKey(GnuhealthInpatientMedication, db_column='name')
    dose = models.FloatField()
    remarks = models.TextField()
    dose_unit = models.ForeignKey(GnuhealthDoseUnit, db_column='dose_unit')
    health_professional = models.ForeignKey(GnuhealthPhysician, db_column='health_professional')
    class Meta:
        db_table = u'gnuhealth_inpatient_medication_log'

class IrModelData(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    noupdate = models.BooleanField()
    db_id = models.IntegerField()
    date_update = models.DateTimeField()
    inherit = models.BooleanField()
    values = models.TextField()
    module = models.CharField(max_length=-1)
    fs_id = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1)
    date_init = models.DateTimeField()
    class Meta:
        db_table = u'ir_model_data'

class GnuhealthDrugsRecreational(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    street_name = models.CharField(max_length=-1)
    addiction_level = models.CharField(max_length=-1)
    route_popping = models.BooleanField()
    category = models.CharField(max_length=-1)
    route_injection = models.BooleanField()
    reinforcement_level = models.IntegerField()
    dependence_level = models.IntegerField()
    dea_schedule_iii = models.BooleanField()
    route_oral = models.BooleanField()
    withdrawal_level = models.IntegerField()
    intoxication_level = models.IntegerField()
    dea_schedule_iv = models.BooleanField()
    dea_schedule_ii = models.BooleanField()
    route_inhaling = models.BooleanField()
    route_sniffing = models.BooleanField()
    info = models.TextField()
    name = models.CharField(max_length=-1)
    dea_schedule_i = models.BooleanField()
    tolerance_level = models.IntegerField()
    legal_status = models.CharField(max_length=-1)
    dea_schedule_v = models.BooleanField()
    toxicity = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_drugs_recreational'

class GnuhealthFamilyMember(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthFamily, db_column='name')
    role = models.CharField(max_length=-1)
    party = models.ForeignKey(PartyParty, db_column='party')
    class Meta:
        db_table = u'gnuhealth_family_member'

class CalendarAttendee(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    attendee = models.TextField() # This field type is a guess.
    status = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1)
    class Meta:
        db_table = u'calendar_attendee'

class GnuhealthPatientRecreationalDrugs(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    recreational_drug = models.ForeignKey(GnuhealthDrugsRecreational, db_column='recreational_drug')
    class Meta:
        db_table = u'gnuhealth_patient_recreational_drugs'

class CalendarEventAttendee(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    calendar_attendee = models.ForeignKey(CalendarAttendee, db_column='calendar_attendee')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    class Meta:
        db_table = u'calendar_event_attendee'

class IrAttachment(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    type = models.CharField(max_length=-1)
    collision = models.IntegerField()
    link = models.CharField(max_length=-1)
    resource = models.CharField(max_length=-1)
    digest = models.CharField(max_length=32)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_attachment'

class GnuhealthDietTherapeutic(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(unique=True, max_length=-1)
    description = models.TextField()
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_diet_therapeutic'

class GnuhealthInpatientDiet(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    diet = models.ForeignKey(GnuhealthDietTherapeutic, db_column='diet')
    remarks = models.TextField()
    class Meta:
        db_table = u'gnuhealth_inpatient_diet'

class GnuhealthInpatientRegistration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    nursing_plan = models.TextField()
    operating_physician = models.ForeignKey(GnuhealthPhysician, db_column='operating_physician')
    diet_vegetarian = models.CharField(max_length=-1)
    discharge_date = models.DateTimeField()
    admission_type = models.CharField(max_length=-1)
    attending_physician = models.ForeignKey(GnuhealthPhysician, db_column='attending_physician')
    discharge_plan = models.TextField()
    state = models.CharField(max_length=-1)
    admission_reason = models.ForeignKey(GnuhealthPathology, db_column='admission_reason')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    info = models.TextField()
    name = models.CharField(max_length=-1)
    hospitalization_date = models.DateTimeField()
    bed = models.ForeignKey(GnuhealthHospitalBed, db_column='bed')
    nutrition_notes = models.TextField()
    diet_belief = models.ForeignKey(GnuhealthDietBelief, db_column='diet_belief')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    icu = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_inpatient_registration'

class GnuhealthMedicamentCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    class Meta:
        db_table = u'gnuhealth_medicament_category'

class IrLang(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    translatable = models.BooleanField()
    active = models.BooleanField()
    direction = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    thousands_sep = models.CharField(max_length=-1)
    date = models.CharField(max_length=-1)
    decimal_point = models.CharField(max_length=-1)
    grouping = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_lang'

class IrCron(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    function = models.CharField(max_length=-1)
    interval_type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    request_user = models.ForeignKey(ResUser, db_column='request_user')
    args = models.TextField()
    number_calls = models.IntegerField()
    model = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUser, db_column='user')
    next_call = models.DateTimeField()
    active = models.BooleanField()
    interval_number = models.IntegerField()
    repeat_missed = models.BooleanField()
    class Meta:
        db_table = u'ir_cron'

class CalendarDate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    datetime = models.DateTimeField()
    date = models.BooleanField()
    class Meta:
        db_table = u'calendar_date'

class GnuhealthPatientCage(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    cage_c = models.BooleanField()
    cage_a = models.BooleanField()
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    cage_e = models.BooleanField()
    cage_score = models.IntegerField()
    cage_g = models.BooleanField()
    evaluation_date = models.DateTimeField()
    class Meta:
        db_table = u'gnuhealth_patient_cage'

class CalendarEventRdate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    calendar_date = models.ForeignKey(CalendarDate, db_column='calendar_date')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    class Meta:
        db_table = u'calendar_event_rdate'

class GnuhealthPatient(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    family = models.ForeignKey(GnuhealthFamily, db_column='family')
    photo = models.TextField() # This field type is a guess.
    sex = models.CharField(max_length=-1)
    blood_type = models.CharField(max_length=-1)
    general_info = models.TextField()
    primary_care_doctor = models.ForeignKey(GnuhealthPhysician, db_column='primary_care_doctor')
    critical_info = models.TextField()
    rh = models.CharField(max_length=-1)
    current_address = models.ForeignKey(PartyAddress, db_column='current_address')
    ethnic_group = models.ForeignKey(GnuhealthEthnicity, db_column='ethnic_group')
    name = models.ForeignKey(PartyParty, db_column='name')
    dob = models.DateField()
    marital_status = models.CharField(max_length=-1)
    dod = models.DateTimeField()
    current_insurance = models.ForeignKey(GnuhealthInsurance, db_column='current_insurance')
    cod = models.ForeignKey(GnuhealthPathology, db_column='cod')
    identification_code = models.CharField(max_length=-1)
    deceased = models.BooleanField()
    works_at_home = models.BooleanField()
    prison_current = models.BooleanField()
    fam_apgar_score = models.IntegerField()
    domestic_violence = models.BooleanField()
    hostile_area = models.BooleanField()
    sexual_abuse = models.BooleanField()
    sewers = models.BooleanField()
    hours_outside = models.IntegerField()
    ses = models.CharField(max_length=-1)
    education = models.CharField(max_length=-1)
    television = models.BooleanField()
    occupation = models.ForeignKey(GnuhealthOccupation, db_column='occupation')
    drug_addiction = models.BooleanField()
    fam_apgar_timesharing = models.CharField(max_length=-1)
    electricity = models.BooleanField()
    housing = models.CharField(max_length=-1)
    school_withdrawal = models.BooleanField()
    income = models.CharField(max_length=-1)
    single_parent = models.BooleanField()
    ses_notes = models.TextField()
    fam_apgar_affection = models.CharField(max_length=-1)
    gas = models.BooleanField()
    internet = models.BooleanField()
    telephone = models.BooleanField()
    water = models.BooleanField()
    fam_apgar_discussion = models.CharField(max_length=-1)
    working_children = models.BooleanField()
    fam_apgar_help = models.CharField(max_length=-1)
    trash = models.BooleanField()
    teenage_pregnancy = models.BooleanField()
    prison_past = models.BooleanField()
    relative_in_prison = models.BooleanField()
    fam_apgar_decisions = models.CharField(max_length=-1)
    full_term = models.IntegerField()
    colposcopy = models.BooleanField()
    breast_self_examination = models.BooleanField()
    pap_test = models.BooleanField()
    mammography = models.BooleanField()
    menopause = models.IntegerField()
    stillbirths = models.IntegerField()
    pap_test_last = models.DateField()
    fertile = models.BooleanField()
    colposcopy_last = models.DateField()
    menopausal = models.BooleanField()
    mammography_last = models.DateField()
    abortions = models.IntegerField()
    premature = models.IntegerField()
    menarche = models.IntegerField()
    gravida = models.IntegerField()
    sexuality_info = models.TextField()
    smoking_number = models.IntegerField()
    sexual_partners = models.CharField(max_length=-1)
    soft_drinks = models.BooleanField()
    coffee = models.BooleanField()
    exercise_minutes_day = models.IntegerField()
    sexual_practices = models.CharField(max_length=-1)
    ex_drug_addict = models.BooleanField()
    sexual_preferences = models.CharField(max_length=-1)
    car_child_safety = models.BooleanField()
    alcohol = models.BooleanField()
    ex_alcoholic = models.BooleanField()
    age_start_drugs = models.IntegerField()
    number_of_meals = models.IntegerField()
    coffee_cups = models.IntegerField()
    exercise = models.BooleanField()
    sex_with_prostitutes = models.BooleanField()
    sleep_during_daytime = models.BooleanField()
    age_quit_smoking = models.IntegerField()
    ex_smoker = models.BooleanField()
    lifestyle_info = models.TextField()
    car_seat_belt = models.BooleanField()
    diet_info = models.CharField(max_length=-1)
    drug_iv = models.BooleanField()
    second_hand_smoker = models.BooleanField()
    age_quit_drugs = models.IntegerField()
    alcohol_liquor_number = models.IntegerField()
    eats_alone = models.BooleanField()
    age_quit_drinking = models.IntegerField()
    sex_oral = models.CharField(max_length=-1)
    home_safety = models.BooleanField()
    age_start_drinking = models.IntegerField()
    first_sexual_encounter = models.IntegerField()
    smoking = models.BooleanField()
    sex_anal = models.CharField(max_length=-1)
    age_start_smoking = models.IntegerField()
    sexual_partners_number = models.IntegerField()
    car_revision = models.BooleanField()
    motorcycle_rider = models.BooleanField()
    helmet = models.BooleanField()
    alcohol_beer_number = models.IntegerField()
    traffic_laws = models.BooleanField()
    sleep_hours = models.IntegerField()
    alcohol_wine_number = models.IntegerField()
    diet = models.BooleanField()
    anticonceptive = models.CharField(max_length=-1)
    prostitute = models.BooleanField()
    salt = models.BooleanField()
    drug_usage = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_patient'

class IrExport(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    resource = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_export'

class IrExportLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    export = models.ForeignKey(IrExport, db_column='export')
    class Meta:
        db_table = u'ir_export_line'

class CalendarEventRrule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    calendar_rrule = models.ForeignKey(CalendarRrule, db_column='calendar_rrule')
    class Meta:
        db_table = u'calendar_event_rrule'

class IrModelField(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.ForeignKey(IrModel, db_column='model')
    name = models.CharField(max_length=-1)
    relation = models.CharField(max_length=-1)
    field_description = models.CharField(max_length=-1)
    ttype = models.CharField(max_length=-1)
    help = models.TextField()
    module = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'ir_model_field'

class IrRuleGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    default_p = models.BooleanField()
    global_p = models.BooleanField()
    perm_create = models.BooleanField()
    perm_write = models.BooleanField()
    perm_read = models.BooleanField()
    model = models.ForeignKey(IrModel, db_column='model')
    perm_delete = models.BooleanField()
    class Meta:
        db_table = u'ir_rule_group'

class CalendarEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    classification = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    transp = models.CharField(max_length=-1)
    timezone = models.CharField(max_length=-1)
    organizer = models.CharField(max_length=-1)
    uuid = models.CharField(max_length=-1)
    recurrence = models.DateTimeField()
    location = models.ForeignKey(CalendarLocation, db_column='location')
    status = models.CharField(max_length=-1)
    description = models.TextField()
    parent = models.ForeignKey('self', db_column='parent')
    dtstart = models.DateTimeField()
    vevent = models.TextField() # This field type is a guess.
    all_day = models.BooleanField()
    dtend = models.DateTimeField()
    summary = models.CharField(max_length=-1)
    calendar = models.ForeignKey(CalendarCalendar, db_column='calendar')
    class Meta:
        db_table = u'calendar_event'

class CalendarRrule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    count = models.IntegerField()
    bysetpos = models.CharField(max_length=-1)
    byday = models.CharField(max_length=-1)
    byminute = models.CharField(max_length=-1)
    byweekno = models.CharField(max_length=-1)
    bymonth = models.CharField(max_length=-1)
    interval = models.IntegerField()
    wkst = models.CharField(max_length=-1)
    bysecond = models.CharField(max_length=-1)
    byyearday = models.CharField(max_length=-1)
    until = models.DateTimeField()
    until_date = models.BooleanField()
    freq = models.CharField(max_length=-1)
    byhour = models.CharField(max_length=-1)
    bymonthday = models.CharField(max_length=-1)
    class Meta:
        db_table = u'calendar_rrule'

class CalendarEventExrule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    event = models.ForeignKey(CalendarEvent, db_column='event')
    calendar_rrule = models.ForeignKey(CalendarRrule, db_column='calendar_rrule')
    class Meta:
        db_table = u'calendar_event_exrule'

class IrRule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    field = models.ForeignKey(IrModelField, db_column='field')
    operator = models.CharField(max_length=-1)
    operand = models.CharField(max_length=-1)
    rule_group = models.ForeignKey(IrRuleGroup, db_column='rule_group')
    class Meta:
        db_table = u'ir_rule'

class GnuhealthLabTestUnits(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_lab_test_units'

class GnuhealthLab(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    date_requested = models.DateTimeField()
    name = models.CharField(unique=True, max_length=-1)
    requestor = models.ForeignKey(GnuhealthPhysician, db_column='requestor')
    date_analysis = models.DateTimeField()
    results = models.TextField()
    pathologist = models.ForeignKey(GnuhealthPhysician, db_column='pathologist')
    diagnosis = models.TextField()
    test = models.ForeignKey(GnuhealthLabTestType, db_column='test')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    class Meta:
        db_table = u'gnuhealth_lab'

class GnuhealthLabTestCritearea(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    result_text = models.CharField(max_length=-1)
    test_type = models.ForeignKey(GnuhealthLabTestType)
    normal_range = models.TextField()
    units = models.ForeignKey(GnuhealthLabTestUnits, db_column='units')
    upper_limit = models.FloatField()
    lower_limit = models.FloatField()
    result = models.FloatField()
    excluded = models.BooleanField()
    remarks = models.CharField(max_length=-1)
    gnuhealth_lab = models.ForeignKey(GnuhealthLab)
    warning = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_lab_test_critearea'

class IrAction(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    usage = models.CharField(max_length=-1)
    active = models.BooleanField()
    type = models.CharField(max_length=-1)
    icon = models.ForeignKey(IrUiIcon, db_column='icon')
    class Meta:
        db_table = u'ir_action'

class IrModuleModuleConfigWizardItem(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    state = models.CharField(max_length=-1)
    action = models.ForeignKey(IrAction, db_column='action')
    class Meta:
        db_table = u'ir_module_module_config_wizard_item'

class GnuhealthDiseaseGene(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    name = models.CharField(max_length=-1)
    gene_id = models.CharField(max_length=-1)
    long_name = models.CharField(max_length=-1)
    location = models.CharField(max_length=-1)
    dominance = models.CharField(max_length=-1)
    chromosome = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_disease_gene'

class GnuhealthPatientGeneticRisk(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    disease_gene = models.ForeignKey(GnuhealthDiseaseGene, db_column='disease_gene')
    class Meta:
        db_table = u'gnuhealth_patient_genetic_risk'

class IrCache(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    timestamp = models.DateTimeField()
    class Meta:
        db_table = u'ir_cache'

class GnuhealthLabTestType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    product = models.ForeignKey(ProductProduct)
    class Meta:
        db_table = u'gnuhealth_lab_test_type'

class IrModel(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(unique=True, max_length=-1)
    name = models.CharField(max_length=-1)
    info = models.TextField()
    module = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'ir_model'

class GnuhealthPatientLabTest(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthLabTestType, db_column='name')
    request = models.IntegerField()
    patient = models.ForeignKey(GnuhealthPatient)
    urgent = models.BooleanField()
    state = models.CharField(max_length=-1)
    date = models.DateTimeField()
    doctor = models.ForeignKey(GnuhealthPhysician)
    class Meta:
        db_table = u'gnuhealth_patient_lab_test'

class GnuhealthPatientFamilyDiseases(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    name = models.ForeignKey(GnuhealthPathology, db_column='name')
    xory = models.CharField(max_length=-1)
    relative = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_patient_family_diseases'

class PartyCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    active = models.BooleanField()
    class Meta:
        db_table = u'party_category'

class IrTrigger(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    on_create = models.BooleanField()
    name = models.CharField(max_length=-1)
    on_delete = models.BooleanField()
    on_time = models.BooleanField()
    action_model = models.ForeignKey(IrModel, db_column='action_model')
    minimum_delay = models.FloatField()
    model = models.ForeignKey(IrModel, db_column='model')
    on_write = models.BooleanField()
    active = models.BooleanField()
    action_function = models.CharField(max_length=-1)
    limit_number = models.IntegerField()
    condition = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_trigger'

class IrTriggerLog(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    trigger = models.ForeignKey(IrTrigger, db_column='trigger')
    record_id = models.IntegerField()
    class Meta:
        db_table = u'ir_trigger_log'

class PartyCategoryRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(PartyCategory, db_column='category')
    party = models.ForeignKey(PartyParty, db_column='party')
    class Meta:
        db_table = u'party_category_rel'

class IrSession(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    key = models.CharField(max_length=-1)
    class Meta:
        db_table = u'ir_session'

class IrSessionWizard(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    data = models.TextField()
    class Meta:
        db_table = u'ir_session_wizard'

class GnuhealthPatientPrenatalEvaluation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    hypertension = models.BooleanField()
    fetal_hc = models.IntegerField()
    evaluation_date = models.DateTimeField()
    efw = models.IntegerField()
    polihydramnios = models.BooleanField()
    fetal_fl = models.IntegerField()
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    oligohydramnios = models.BooleanField()
    fetal_bpd = models.IntegerField()
    vasa_previa = models.BooleanField()
    overweight = models.BooleanField()
    iugr = models.BooleanField()
    placenta_previa = models.BooleanField()
    preeclampsia = models.BooleanField()
    diabetes = models.BooleanField()
    name = models.ForeignKey(GnuhealthPatientPregnancy, db_column='name')
    fetal_ac = models.IntegerField()
    fundal_height = models.IntegerField()
    fetus_heart_rate = models.IntegerField()
    invasive_placentation = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_patient_prenatal_evaluation'

class GnuhealthPathologyCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    class Meta:
        db_table = u'gnuhealth_pathology_category'

class GnuhealthSurgery(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    preop_site_marking = models.BooleanField()
    code = models.CharField(max_length=-1)
    classification = models.CharField(max_length=-1)
    pathology = models.ForeignKey(GnuhealthPathology, db_column='pathology')
    extra_info = models.TextField()
    preop_bleeding_risk = models.BooleanField()
    preop_antibiotics = models.BooleanField()
    admission = models.ForeignKey(GnuhealthAppointment, db_column='admission')
    preop_sterility = models.BooleanField()
    anesthetist = models.ForeignKey(GnuhealthPhysician, db_column='anesthetist')
    preop_mallampati = models.CharField(max_length=-1)
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    description = models.CharField(max_length=-1)
    date = models.DateTimeField()
    surgeon = models.ForeignKey(GnuhealthPhysician, db_column='surgeon')
    age = models.CharField(max_length=-1)
    operating_room = models.ForeignKey(GnuhealthHospitalOr, db_column='operating_room')
    preop_oximeter = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_surgery'

class ResUserIrAction(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser, db_column='user')
    action = models.ForeignKey(IrAction, db_column='action')
    class Meta:
        db_table = u'res_user-ir_action'

class GnuhealthOperation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthSurgery, db_column='name')
    notes = models.TextField()
    procedure = models.ForeignKey(GnuhealthProcedure, db_column='procedure')
    class Meta:
        db_table = u'gnuhealth_operation'

class GnuhealthPathologyGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    desc = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_pathology_group'

class GnuhealthDiseaseGroupMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    disease_group = models.ForeignKey(GnuhealthPathologyGroup, db_column='disease_group')
    name = models.ForeignKey(GnuhealthPathology, db_column='name')
    class Meta:
        db_table = u'gnuhealth_disease_group_members'

class GnuhealthPuerperiumMonitor(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientPregnancy, db_column='name')
    lochia_odor = models.CharField(max_length=-1)
    frequency = models.IntegerField()
    lochia_color = models.CharField(max_length=-1)
    temperature = models.FloatField()
    date = models.DateTimeField()
    systolic = models.IntegerField()
    uterus_involution = models.IntegerField()
    lochia_amount = models.CharField(max_length=-1)
    diastolic = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_puerperium_monitor'

class ResUserWarning(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    always = models.BooleanField()
    user = models.ForeignKey(ResUser, db_column='user')
    class Meta:
        db_table = u'res_user_warning'

class GnuhealthPatientPregnancy(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    gravida = models.IntegerField()
    fetuses = models.IntegerField()
    lmp = models.DateField()
    pregnancy_end_result = models.CharField(max_length=-1)
    monozygotic = models.BooleanField()
    pregnancy_end_date = models.DateTimeField()
    iugr = models.CharField(max_length=-1)
    current_pregnancy = models.BooleanField()
    warning = models.BooleanField()
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    class Meta:
        db_table = u'gnuhealth_patient_pregnancy'

class ResRequestLink(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    priority = models.IntegerField()
    model = models.CharField(max_length=-1)
    class Meta:
        db_table = u'res_request_link'

class GnuhealthPerinatal(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    abruptio_placentae = models.BooleanField()
    abortion = models.BooleanField()
    stillbirth = models.BooleanField()
    placenta_retained = models.BooleanField()
    vaginal_tearing = models.BooleanField()
    prenatal_evaluations = models.IntegerField()
    start_labor_mode = models.CharField(max_length=-1)
    gestational_days = models.IntegerField()
    laceration = models.CharField(max_length=-1)
    hematoma = models.CharField(max_length=-1)
    forceps = models.BooleanField()
    dismissed = models.DateTimeField()
    gravida_number = models.IntegerField()
    place_of_death = models.CharField(max_length=-1)
    admission_code = models.CharField(max_length=-1)
    dystocia = models.BooleanField()
    fetus_presentation = models.CharField(max_length=-1)
    episiotomy = models.BooleanField()
    name = models.ForeignKey(GnuhealthPatientPregnancy, db_column='name')
    mother_deceased = models.BooleanField()
    notes = models.TextField()
    admission_date = models.DateTimeField()
    placenta_incomplete = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_perinatal'

class GnuhealthInsurancePlan(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(ProductProduct, db_column='name')
    company = models.ForeignKey(PartyParty, db_column='company')
    is_default = models.BooleanField()
    notes = models.TextField()
    class Meta:
        db_table = u'gnuhealth_insurance_plan'

class AccountInvoicePaymentTermLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    weeks = models.IntegerField()
    divisor = models.DecimalField(max_digits=65535, decimal_places=65535)
    sequence = models.IntegerField()
    payment = models.ForeignKey(AccountInvoicePaymentTerm, db_column='payment')
    months = models.IntegerField()
    days = models.IntegerField()
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    weekday = models.CharField(max_length=-1)
    percentage = models.DecimalField(max_digits=65535, decimal_places=65535)
    month = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    day = models.IntegerField()
    class Meta:
        db_table = u'account_invoice_payment_term_line'

class GnuhealthPerinatalMonitor(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    contractions = models.IntegerField()
    name = models.ForeignKey(GnuhealthPerinatal, db_column='name')
    bleeding = models.BooleanField()
    meconium = models.BooleanField()
    fetus_position = models.CharField(max_length=-1)
    frequency = models.IntegerField()
    f_frequency = models.IntegerField()
    date = models.DateTimeField()
    systolic = models.IntegerField()
    fundal_height = models.IntegerField()
    dilation = models.IntegerField()
    diastolic = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_perinatal_monitor'

class ResRequestHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    body = models.TextField()
    name = models.CharField(max_length=-1)
    request = models.ForeignKey(ResRequest, db_column='request')
    number_references = models.IntegerField()
    priority = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    act_from = models.ForeignKey(ResUser, db_column='act_from')
    date_sent = models.DateTimeField()
    act_to = models.ForeignKey(ResUser, db_column='act_to')
    subject = models.CharField(max_length=-1)
    class Meta:
        db_table = u'res_request_history'

class AccountInvoicePaymentTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    active = models.BooleanField()
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_invoice_payment_term'

class ResRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    body = models.TextField()
    name = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1)
    date_sent = models.DateTimeField()
    state = models.CharField(max_length=-1)
    act_from = models.ForeignKey(ResUser, db_column='act_from')
    active = models.BooleanField()
    trigger_date = models.DateTimeField()
    act_to = models.ForeignKey(ResUser, db_column='act_to')
    class Meta:
        db_table = u'res_request'

class ResRequestReference(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    reference = models.CharField(max_length=-1)
    request = models.ForeignKey(ResRequest, db_column='request')
    class Meta:
        db_table = u'res_request_reference'

class GnuhealthPatientMenstrualHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    lmp_length = models.IntegerField()
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    is_regular = models.BooleanField()
    lmp = models.DateField()
    dysmenorrhea = models.BooleanField()
    volume = models.CharField(max_length=-1)
    frequency = models.CharField(max_length=-1)
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    evaluation_date = models.DateField()
    class Meta:
        db_table = u'gnuhealth_patient_menstrual_history'

class GnuhealthSequences(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'gnuhealth_sequences'

class IrUiMenuResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    menu = models.ForeignKey(IrUiMenu, db_column='menu')
    group = models.ForeignKey(ResGroup, db_column='group')
    class Meta:
        db_table = u'ir_ui_menu-res_group'

class GnuhealthPatientMammographyHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    comments = models.CharField(max_length=-1)
    last_mammography = models.DateField()
    result = models.CharField(max_length=-1)
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    evaluation_date = models.DateField()
    class Meta:
        db_table = u'gnuhealth_patient_mammography_history'

class GnuhealthFamily(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    name = models.CharField(unique=True, max_length=-1)
    operational_sector = models.ForeignKey(GnuhealthOperationalSector, db_column='operational_sector')
    class Meta:
        db_table = u'gnuhealth_family'

class IrActionResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    action = models.ForeignKey(IrAction, db_column='action')
    group = models.ForeignKey(ResGroup, db_column='group')
    class Meta:
        db_table = u'ir_action-res_group'

class IrModelFieldResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    field = models.ForeignKey(IrModelField)
    group = models.ForeignKey(ResGroup)
    class Meta:
        db_table = u'ir_model_field-res_group'

class GnuhealthEthnicity(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(unique=True, max_length=-1)
    notes = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_ethnicity'

class GnuhealthPatientPapHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    last_pap = models.DateField()
    comments = models.CharField(max_length=-1)
    result = models.CharField(max_length=-1)
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    evaluation_date = models.DateField()
    class Meta:
        db_table = u'gnuhealth_patient_pap_history'

class GnuhealthInsurance(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.CharField(max_length=-1)
    insurance_type = models.CharField(max_length=-1)
    member_since = models.DateField()
    company = models.ForeignKey(PartyParty, db_column='company')
    number = models.CharField(max_length=-1)
    member_exp = models.DateField()
    notes = models.TextField()
    plan = models.ForeignKey(GnuhealthInsurancePlan)
    name = models.ForeignKey(PartyParty, db_column='name')
    class Meta:
        db_table = u'gnuhealth_insurance'

class AccountInvoiceAccountMoveLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    invoice = models.ForeignKey(AccountInvoice, db_column='invoice')
    line = models.ForeignKey(AccountMoveLine, db_column='line')
    class Meta:
        db_table = u'account_invoice-account_move_line'

class IrModelButtonResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    button = models.ForeignKey(IrModelButton, db_column='button')
    active = models.BooleanField()
    group = models.ForeignKey(ResGroup, db_column='group')
    class Meta:
        db_table = u'ir_model_button-res_group'

class GnuhealthPatientColposcopyHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    last_colposcopy = models.DateField()
    comments = models.CharField(max_length=-1)
    result = models.CharField(max_length=-1)
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    evaluation_date = models.DateField()
    class Meta:
        db_table = u'gnuhealth_patient_colposcopy_history'

class IrRuleGroupResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    group = models.ForeignKey(ResGroup, db_column='group')
    rule_group = models.ForeignKey(IrRuleGroup, db_column='rule_group')
    class Meta:
        db_table = u'ir_rule_group-res_group'

class GnuhealthPatientDisease(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    treatment_description = models.CharField(max_length=-1)
    healed_date = models.DateField()
    pathology = models.ForeignKey(GnuhealthPathology, db_column='pathology')
    disease_severity = models.CharField(max_length=-1)
    is_allergy = models.BooleanField()
    doctor = models.ForeignKey(GnuhealthPhysician, db_column='doctor')
    pregnancy_warning = models.BooleanField()
    weeks_of_pregnancy = models.IntegerField()
    is_on_treatment = models.BooleanField()
    diagnosed_date = models.DateField()
    extra_info = models.TextField()
    status = models.CharField(max_length=-1)
    is_active = models.BooleanField()
    date_stop_treatment = models.DateField()
    pcs_code = models.ForeignKey(GnuhealthProcedure, db_column='pcs_code')
    is_infectious = models.BooleanField()
    allergy_type = models.CharField(max_length=-1)
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    age = models.IntegerField()
    date_start_treatment = models.DateField()
    short_comment = models.CharField(max_length=-1)
    newborn = models.ForeignKey(GnuhealthNewborn)
    class Meta:
        db_table = u'gnuhealth_patient_disease'

class IrRuleGroupResUser(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser, db_column='user')
    rule_group = models.ForeignKey(IrRuleGroup, db_column='rule_group')
    class Meta:
        db_table = u'ir_rule_group-res_user'

class IrSequenceTypeResGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence_type = models.ForeignKey(IrSequenceType, db_column='sequence_type')
    group = models.ForeignKey(ResGroup, db_column='group')
    class Meta:
        db_table = u'ir_sequence_type-res_group'

class AccountInvoiceLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    invoice = models.ForeignKey(AccountInvoice, db_column='invoice')
    unit = models.ForeignKey(ProductUom, db_column='unit')
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    note = models.TextField()
    party = models.ForeignKey(PartyParty, db_column='party')
    type = models.CharField(max_length=-1)
    product = models.ForeignKey(ProductProduct, db_column='product')
    description = models.TextField()
    invoice_type = models.CharField(max_length=-1)
    company = models.ForeignKey(CompanyCompany, db_column='company')
    account = models.ForeignKey(AccountAccount, db_column='account')
    quantity = models.FloatField()
    class Meta:
        db_table = u'account_invoice_line'

class AccountInvoiceLineAccountTax(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    line = models.ForeignKey(AccountInvoiceLine, db_column='line')
    class Meta:
        db_table = u'account_invoice_line_account_tax'

class AccountInvoice(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    comment = models.TextField()
    reference = models.CharField(max_length=-1)
    payment_term = models.ForeignKey(AccountInvoicePaymentTerm, db_column='payment_term')
    move = models.ForeignKey(AccountMove, db_column='move')
    number = models.CharField(max_length=-1)
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    description = models.CharField(max_length=-1)
    invoice_report_format = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    party = models.ForeignKey(PartyParty, db_column='party')
    type = models.CharField(max_length=-1)
    company = models.ForeignKey(CompanyCompany, db_column='company')
    invoice_report_cache = models.TextField() # This field type is a guess.
    journal = models.ForeignKey(AccountJournal, db_column='journal')
    invoice_date = models.DateField()
    account = models.ForeignKey(AccountAccount, db_column='account')
    accounting_date = models.DateField()
    invoice_address = models.ForeignKey(PartyAddress, db_column='invoice_address')
    class Meta:
        db_table = u'account_invoice'

class GnuhealthMedicationDosage(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    abbreviation = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_medication_dosage'

class GnuhealthDrugForm(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_drug_form'

class GnuhealthMedicament(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(GnuhealthMedicamentCategory, db_column='category')
    indications = models.TextField()
    therapeutic_action = models.CharField(max_length=-1)
    name = models.ForeignKey(ProductProduct, db_column='name')
    pregnancy_category = models.CharField(max_length=-1)
    overdosage = models.TextField()
    pregnancy_warning = models.BooleanField()
    notes = models.TextField()
    storage = models.TextField()
    adverse_reaction = models.TextField()
    active_component = models.CharField(max_length=-1)
    dosage = models.TextField()
    pregnancy = models.TextField()
    presentation = models.TextField()
    composition = models.TextField()
    class Meta:
        db_table = u'gnuhealth_medicament'

class GnuhealthDrugRoute(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_drug_route'

class AccountInvoiceTax(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccount, db_column='account')
    description = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    tax = models.ForeignKey(AccountTax, db_column='tax')
    manual = models.BooleanField()
    base_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    tax_code = models.ForeignKey(AccountTaxCode, db_column='tax_code')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    base = models.DecimalField(max_digits=65535, decimal_places=65535)
    invoice = models.ForeignKey(AccountInvoice, db_column='invoice')
    base_code = models.ForeignKey(AccountTaxCode, db_column='base_code')
    tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    class Meta:
        db_table = u'account_invoice_tax'

class PartyAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    city = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    zip = models.CharField(max_length=-1)
    country = models.ForeignKey(CountryCountry, db_column='country')
    sequence = models.IntegerField()
    subdivision = models.ForeignKey(CountrySubdivision, db_column='subdivision')
    streetbis = models.CharField(max_length=-1)
    street = models.CharField(max_length=-1)
    active = models.BooleanField()
    party = models.ForeignKey(PartyParty, db_column='party')
    relationship = models.CharField(max_length=-1)
    relative = models.ForeignKey(PartyParty)
    is_work = models.BooleanField()
    is_school = models.BooleanField()
    delivery = models.BooleanField()
    invoice = models.BooleanField()
    class Meta:
        db_table = u'party_address'

class GnuhealthDoseUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    desc = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_dose_unit'

class IrSequenceStrict(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    last_timestamp = models.IntegerField()
    number_next_internal = models.IntegerField()
    timestamp_rounding = models.FloatField()
    padding = models.IntegerField()
    number_increment = models.IntegerField()
    prefix = models.CharField(max_length=-1)
    timestamp_offset = models.FloatField()
    active = models.BooleanField()
    type = models.CharField(max_length=-1)
    suffix = models.CharField(max_length=-1)
    company = models.ForeignKey(CompanyCompany, db_column='company')
    class Meta:
        db_table = u'ir_sequence_strict'

class GnuhealthPatientMedication(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    doctor = models.ForeignKey(GnuhealthPhysician, db_column='doctor')
    is_active = models.BooleanField()
    notes = models.TextField()
    adverse_reaction = models.TextField()
    course_completed = models.BooleanField()
    template = models.ForeignKey(GnuhealthMedicationTemplate, db_column='template')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    discontinued_reason = models.CharField(max_length=-1)
    discontinued = models.BooleanField()
    newborn = models.ForeignKey(GnuhealthNewborn)
    class Meta:
        db_table = u'gnuhealth_patient_medication'

class GnuhealthRoundingProcedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientRounding, db_column='name')
    notes = models.TextField()
    procedure = models.ForeignKey(GnuhealthProcedure, db_column='procedure')
    class Meta:
        db_table = u'gnuhealth_rounding_procedure'

class GnuhealthVaccination(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    vaccine_lot = models.CharField(max_length=-1)
    name = models.ForeignKey(GnuhealthPatient, db_column='name')
    vaccine = models.ForeignKey(ProductProduct, db_column='vaccine')
    institution = models.ForeignKey(PartyParty, db_column='institution')
    observations = models.CharField(max_length=-1)
    date = models.DateTimeField()
    dose = models.IntegerField()
    next_dose_date = models.DateTimeField()
    vaccine_expiration_date = models.DateField()
    class Meta:
        db_table = u'gnuhealth_vaccination'

class GnuhealthPatientAmbulatoryCare(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    session_number = models.IntegerField()
    warning = models.BooleanField()
    next_session = models.DateTimeField()
    health_professional = models.ForeignKey(GnuhealthPhysician, db_column='health_professional')
    session_start = models.DateTimeField()
    temperature = models.FloatField()
    session_end = models.DateTimeField()
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    diastolic = models.IntegerField()
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    glycemia = models.IntegerField()
    respiratory_rate = models.IntegerField()
    base_condition = models.ForeignKey(GnuhealthPathology, db_column='base_condition')
    osat = models.IntegerField()
    evolution = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    bpm = models.IntegerField()
    systolic = models.IntegerField()
    ordering_professional = models.ForeignKey(GnuhealthPhysician, db_column='ordering_professional')
    session_notes = models.TextField()
    care_location = models.ForeignKey(StockLocation, db_column='care_location')
    state = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_patient_ambulatory_care'

class ResUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    active = models.BooleanField()
    login = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey('self', db_column='create_uid')
    write_uid = models.ForeignKey('self', db_column='write_uid')
    timezone = models.CharField(max_length=-1)
    menu = models.ForeignKey(IrAction, db_column='menu')
    email = models.CharField(max_length=-1)
    language = models.ForeignKey(IrLang, db_column='language')
    login_try = models.IntegerField()
    signature = models.TextField()
    salt = models.CharField(max_length=8)
    main_company = models.ForeignKey(CompanyCompany, db_column='main_company')
    employee = models.ForeignKey(CompanyEmployee, db_column='employee')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    class Meta:
        db_table = u'res_user'

class GnuhealthPrescriptionOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    user = models.ForeignKey(ResUser)
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    doctor = models.ForeignKey(GnuhealthPhysician, db_column='doctor')
    pregnancy_warning = models.BooleanField()
    notes = models.TextField()
    pharmacy = models.ForeignKey(PartyParty, db_column='pharmacy')
    prescription_date = models.DateTimeField()
    prescription_warning_ack = models.BooleanField()
    prescription_id = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_prescription_order'

class GnuhealthAmbulatoryCareProcedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientAmbulatoryCare, db_column='name')
    comments = models.CharField(max_length=-1)
    procedure = models.ForeignKey(GnuhealthProcedure, db_column='procedure')
    class Meta:
        db_table = u'gnuhealth_ambulatory_care_procedure'

class GnuhealthMedicationTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    frequency_prn = models.BooleanField()
    frequency = models.IntegerField()
    duration = models.IntegerField()
    admin_times = models.CharField(max_length=-1)
    end_treatment = models.DateTimeField()
    dose = models.FloatField()
    form = models.ForeignKey(GnuhealthDrugForm, db_column='form')
    common_dosage = models.ForeignKey(GnuhealthMedicationDosage, db_column='common_dosage')
    medicament = models.ForeignKey(GnuhealthMedicament, db_column='medicament')
    qty = models.IntegerField()
    dose_unit = models.ForeignKey(GnuhealthDoseUnit, db_column='dose_unit')
    start_treatment = models.DateTimeField()
    duration_period = models.CharField(max_length=-1)
    frequency_unit = models.CharField(max_length=-1)
    indication = models.ForeignKey(GnuhealthPathology, db_column='indication')
    route = models.ForeignKey(GnuhealthDrugRoute, db_column='route')
    class Meta:
        db_table = u'gnuhealth_medication_template'

class GnuhealthPrescriptionLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPrescriptionOrder, db_column='name')
    allow_substitution = models.BooleanField()
    prnt = models.BooleanField()
    review = models.DateTimeField()
    short_comment = models.CharField(max_length=-1)
    template = models.ForeignKey(GnuhealthMedicationTemplate, db_column='template')
    refills = models.IntegerField()
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_prescription_line'

class GnuhealthHealthService(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    name = models.CharField(unique=True, max_length=-1)
    state = models.CharField(max_length=-1)
    service_date = models.DateField()
    desc = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_health_service'

class GnuhealthAppointment(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    consultations = models.ForeignKey(ProductProduct, db_column='consultations')
    name = models.CharField(max_length=-1)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(GnuhealthPhysician, db_column='doctor')
    comments = models.TextField()
    institution = models.ForeignKey(PartyParty, db_column='institution')
    appointment_type = models.CharField(max_length=-1)
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    urgency = models.CharField(max_length=-1)
    speciality = models.ForeignKey(GnuhealthSpecialty, db_column='speciality')
    inpatient_registration_code = models.ForeignKey(GnuhealthInpatientRegistration, db_column='inpatient_registration_code')
    appointment_time = models.IntegerField()
    event = models.ForeignKey(CalendarEvent, db_column='event')
    class Meta:
        db_table = u'gnuhealth_appointment'

class GnuhealthHealthServiceLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    name = models.ForeignKey(GnuhealthHealthService, db_column='name')
    qty = models.IntegerField()
    to_invoice = models.BooleanField()
    from_date = models.DateField()
    to_date = models.DateField()
    appointment = models.ForeignKey(GnuhealthAppointment, db_column='appointment')
    desc = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_health_service_line'

class GnuhealthSpecialty(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(unique=True, max_length=-1)
    class Meta:
        db_table = u'gnuhealth_specialty'

class GnuhealthPhysician(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    info = models.TextField()
    code = models.CharField(max_length=-1)
    name = models.ForeignKey(PartyParty, db_column='name')
    specialty = models.ForeignKey(GnuhealthSpecialty, db_column='specialty')
    institution = models.ForeignKey(PartyParty, db_column='institution')
    calendar = models.ForeignKey(CalendarCalendar, db_column='calendar')
    class Meta:
        db_table = u'gnuhealth_physician'

class GnuhealthIcuVentilation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    ett_size = models.IntegerField()
    mv_end = models.DateTimeField()
    mv_start = models.DateTimeField()
    tracheostomy_size = models.IntegerField()
    ventilation = models.CharField(max_length=-1)
    current_mv = models.BooleanField()
    remarks = models.CharField(max_length=-1)
    name = models.ForeignKey(GnuhealthInpatientIcu, db_column='name')
    class Meta:
        db_table = u'gnuhealth_icu_ventilation'

class GnuhealthProcedure(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_procedure'

class GnuhealthIcuApache2(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    pao2 = models.IntegerField()
    serum_potassium = models.FloatField()
    paco2 = models.IntegerField()
    fio2 = models.FloatField()
    apache_score = models.IntegerField()
    arf = models.BooleanField()
    score_date = models.DateTimeField()
    serum_sodium = models.IntegerField()
    chronic_condition = models.BooleanField()
    hematocrit = models.FloatField()
    temperature = models.FloatField()
    serum_creatinine = models.FloatField()
    aado2 = models.IntegerField()
    gcs = models.IntegerField()
    mean_ap = models.IntegerField()
    ph = models.FloatField()
    hospital_admission_type = models.CharField(max_length=-1)
    respiratory_rate = models.IntegerField()
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    age = models.IntegerField()
    heart_rate = models.IntegerField()
    wbc = models.FloatField()
    class Meta:
        db_table = u'gnuhealth_icu_apache2'

class GnuhealthDirections(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientEvaluation, db_column='name')
    comments = models.CharField(max_length=-1)
    procedure = models.ForeignKey(GnuhealthProcedure, db_column='procedure')
    class Meta:
        db_table = u'gnuhealth_directions'

class GnuhealthInpatientIcu(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    icu_discharge_date = models.DateTimeField()
    admitted = models.BooleanField()
    icu_admission_date = models.DateTimeField()
    discharged_from_icu = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_inpatient_icu'

class GnuhealthSecondaryCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    comments = models.CharField(max_length=-1)
    pathology = models.ForeignKey(GnuhealthPathology, db_column='pathology')
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    class Meta:
        db_table = u'gnuhealth_secondary_condition'

class GnuhealthIcuChestDrainage(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientRounding, db_column='name')
    air_leak = models.BooleanField()
    fluid_aspect = models.CharField(max_length=-1)
    fluid_volume = models.IntegerField()
    suction_pressure = models.IntegerField()
    location = models.CharField(max_length=-1)
    remarks = models.CharField(max_length=-1)
    suction = models.BooleanField()
    oscillation = models.BooleanField()
    class Meta:
        db_table = u'gnuhealth_icu_chest_drainage'

class GnuhealthDiagnosticHypothesis(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    comments = models.CharField(max_length=-1)
    pathology = models.ForeignKey(GnuhealthPathology, db_column='pathology')
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    class Meta:
        db_table = u'gnuhealth_diagnostic_hypothesis'

class GnuhealthPatientEvaluation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    information_source = models.CharField(max_length=-1)
    info_diagnosis = models.TextField()
    orientation = models.BooleanField()
    weight = models.FloatField()
    evaluation_type = models.CharField(max_length=-1)
    malnutrition = models.BooleanField()
    height = models.FloatField()
    dehydration = models.BooleanField()
    tag = models.IntegerField()
    tremor = models.BooleanField()
    present_illness = models.TextField()
    evaluation_date = models.ForeignKey(GnuhealthAppointment, db_column='evaluation_date')
    evaluation_start = models.DateTimeField()
    user = models.ForeignKey(ResUser)
    mood = models.CharField(max_length=-1)
    doctor = models.ForeignKey(GnuhealthPhysician, db_column='doctor')
    knowledge_current_events = models.BooleanField()
    loc_verbal = models.CharField(max_length=-1)
    next_evaluation = models.ForeignKey(GnuhealthAppointment, db_column='next_evaluation')
    loc_motor = models.CharField(max_length=-1)
    reliable_info = models.BooleanField()
    systolic = models.IntegerField()
    vocabulary = models.BooleanField()
    praxis = models.BooleanField()
    hip = models.FloatField()
    memory = models.BooleanField()
    abstraction = models.BooleanField()
    patient = models.ForeignKey(GnuhealthPatient, db_column='patient')
    derived_from = models.ForeignKey(GnuhealthPhysician, db_column='derived_from')
    specialty = models.ForeignKey(GnuhealthSpecialty, db_column='specialty')
    loc = models.IntegerField()
    glycemia = models.FloatField()
    head_circumference = models.FloatField()
    bmi = models.FloatField()
    respiratory_rate = models.IntegerField()
    derived_to = models.ForeignKey(GnuhealthPhysician, db_column='derived_to')
    hba1c = models.FloatField()
    violent = models.BooleanField()
    directions = models.TextField()
    evaluation_summary = models.TextField()
    cholesterol_total = models.IntegerField()
    judgment = models.BooleanField()
    temperature = models.FloatField()
    osat = models.IntegerField()
    evaluation_endtime = models.DateTimeField()
    notes = models.TextField()
    calculation_ability = models.BooleanField()
    bpm = models.IntegerField()
    chief_complaint = models.CharField(max_length=-1)
    loc_eyes = models.CharField(max_length=-1)
    abdominal_circ = models.FloatField()
    object_recognition = models.BooleanField()
    diagnosis = models.ForeignKey(GnuhealthPathology, db_column='diagnosis')
    whr = models.FloatField()
    ldl = models.IntegerField()
    notes_complaint = models.TextField()
    hdl = models.IntegerField()
    diastolic = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_evaluation'

class GnuhealthPathology(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    category = models.ForeignKey(GnuhealthPathologyCategory, db_column='category')
    code = models.CharField(unique=True, max_length=-1)
    name = models.CharField(max_length=-1)
    info = models.TextField()
    protein = models.CharField(max_length=-1)
    gene = models.CharField(max_length=-1)
    chromosome = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_pathology'

class GnuhealthSignsAndSymptoms(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    comments = models.CharField(max_length=-1)
    clinical = models.ForeignKey(GnuhealthPathology, db_column='clinical')
    sign_or_symptom = models.CharField(max_length=-1)
    evaluation = models.ForeignKey(GnuhealthPatientEvaluation, db_column='evaluation')
    class Meta:
        db_table = u'gnuhealth_signs_and_symptoms'

class GnuhealthIcuGlasgow(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    glasgow_eyes = models.CharField(max_length=-1)
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    glasgow_motor = models.CharField(max_length=-1)
    glasgow_verbal = models.CharField(max_length=-1)
    glasgow = models.IntegerField()
    evaluation_date = models.DateTimeField()
    class Meta:
        db_table = u'gnuhealth_icu_glasgow'

class GnuhealthIcuEcg(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    pr = models.IntegerField()
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    lead = models.CharField(max_length=-1)
    rhythm = models.CharField(max_length=-1)
    ecg_date = models.DateTimeField()
    ecg_strip = models.TextField() # This field type is a guess.
    rate = models.IntegerField()
    qrs = models.IntegerField()
    pacemaker = models.CharField(max_length=-1)
    st_segment = models.CharField(max_length=-1)
    interpretation = models.CharField(max_length=-1)
    twave_inversion = models.BooleanField()
    qt = models.IntegerField()
    axis = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_icu_ecg'

class GnuhealthPatientAmbulatoryCareMedicament(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    name = models.ForeignKey(GnuhealthPatientAmbulatoryCare, db_column='name')
    short_comment = models.CharField(max_length=-1)
    lot = models.ForeignKey(StockLot, db_column='lot')
    medicament = models.ForeignKey(GnuhealthMedicament, db_column='medicament')
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_ambulatory_care_medicament'

class GnuhealthPatientAmbulatoryCareMedicalSupply(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    name = models.ForeignKey(GnuhealthPatientAmbulatoryCare, db_column='name')
    short_comment = models.CharField(max_length=-1)
    lot = models.ForeignKey(StockLot, db_column='lot')
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_ambulatory_care_medical_supply'

class GnuhealthHospitalOr(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    building = models.ForeignKey(GnuhealthHospitalBuilding, db_column='building')
    name = models.CharField(max_length=-1)
    institution = models.ForeignKey(PartyParty, db_column='institution')
    unit = models.ForeignKey(GnuhealthHospitalUnit, db_column='unit')
    extra_info = models.TextField()
    class Meta:
        db_table = u'gnuhealth_hospital_or'

class GnuhealthPatientAmbulatoryCareVaccine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientAmbulatoryCare, db_column='name')
    short_comment = models.CharField(max_length=-1)
    dose = models.IntegerField()
    vaccine = models.ForeignKey(ProductProduct, db_column='vaccine')
    lot = models.ForeignKey(StockLot, db_column='lot')
    next_dose_date = models.DateTimeField()
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_ambulatory_care_vaccine'

class PartyParty(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    vat_number = models.CharField(max_length=-1)
    code_length = models.IntegerField()
    vat_country = models.CharField(max_length=-1)
    active = models.BooleanField()
    lang = models.ForeignKey(IrLang, db_column='lang')
    name = models.CharField(max_length=-1)
    is_doctor = models.BooleanField()
    insurance_company_type = models.CharField(max_length=-1)
    internal_user = models.ForeignKey(ResUser, db_column='internal_user')
    activation_date = models.DateField()
    is_patient = models.BooleanField()
    is_insurance_company = models.BooleanField()
    ref = models.CharField(unique=True, max_length=-1)
    lastname = models.CharField(max_length=-1)
    is_institution = models.BooleanField()
    is_pharmacy = models.BooleanField()
    alias = models.CharField(max_length=-1)
    is_person = models.BooleanField()
    warehouse = models.ForeignKey(StockLocation, db_column='warehouse')
    class Meta:
        db_table = u'party_party'

class GnuhealthHospitalUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    institution = models.ForeignKey(PartyParty, db_column='institution')
    extra_info = models.TextField()
    class Meta:
        db_table = u'gnuhealth_hospital_unit'

class GnuhealthPatientRoundingMedicament(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    name = models.ForeignKey(GnuhealthPatientRounding, db_column='name')
    short_comment = models.CharField(max_length=-1)
    lot = models.ForeignKey(StockLot, db_column='lot')
    medicament = models.ForeignKey(GnuhealthMedicament, db_column='medicament')
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_rounding_medicament'

class GnuhealthHospitalBuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    institution = models.ForeignKey(PartyParty, db_column='institution')
    extra_info = models.TextField()
    class Meta:
        db_table = u'gnuhealth_hospital_building'

class GnuhealthHospitalBed(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(ProductProduct, db_column='name')
    bed_type = models.CharField(max_length=-1)
    telephone_number = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    ward = models.ForeignKey(GnuhealthHospitalWard, db_column='ward')
    extra_info = models.TextField()
    calendar = models.ForeignKey(CalendarCalendar, db_column='calendar')
    class Meta:
        db_table = u'gnuhealth_hospital_bed'

class GnuhealthPatientRoundingMedicalSupply(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    name = models.ForeignKey(GnuhealthPatientRounding, db_column='name')
    short_comment = models.CharField(max_length=-1)
    lot = models.ForeignKey(StockLot, db_column='lot')
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_rounding_medical_supply'

class GnuhealthHospitalWard(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    ac = models.BooleanField()
    telephone = models.BooleanField()
    private = models.BooleanField()
    guest_sofa = models.BooleanField()
    bio_hazard = models.BooleanField()
    unit = models.ForeignKey(GnuhealthHospitalUnit, db_column='unit')
    extra_info = models.TextField()
    floor = models.IntegerField()
    tv = models.BooleanField()
    microwave = models.BooleanField()
    state = models.CharField(max_length=-1)
    number_of_beds = models.IntegerField()
    internet = models.BooleanField()
    private_bathroom = models.BooleanField()
    institution = models.ForeignKey(PartyParty, db_column='institution')
    refrigerator = models.BooleanField()
    building = models.ForeignKey(GnuhealthHospitalBuilding, db_column='building')
    name = models.CharField(max_length=-1)
    gender = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_hospital_ward'

class GnuhealthPatientRounding(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    round_summary = models.TextField()
    proximity = models.BooleanField()
    warning = models.BooleanField()
    urinary_catheter = models.BooleanField()
    personal_needs = models.BooleanField()
    depression = models.BooleanField()
    evaluation_start = models.DateTimeField()
    diuresis = models.IntegerField()
    evaluation_end = models.DateTimeField()
    temperature = models.FloatField()
    pain_level = models.IntegerField()
    potty = models.BooleanField()
    pump = models.BooleanField()
    health_professional = models.ForeignKey(GnuhealthPhysician, db_column='health_professional')
    pain = models.BooleanField()
    glycemia = models.IntegerField()
    respiratory_rate = models.IntegerField()
    osat = models.IntegerField()
    evolution = models.CharField(max_length=-1)
    name = models.ForeignKey(GnuhealthInpatientRegistration, db_column='name')
    environmental_assessment = models.CharField(max_length=-1)
    bpm = models.IntegerField()
    systolic = models.IntegerField()
    position = models.BooleanField()
    diastolic = models.IntegerField()
    edema = models.CharField(max_length=-1)
    sce = models.BooleanField()
    fio2 = models.IntegerField()
    lips_lesion = models.BooleanField()
    pupillary_reactivity = models.CharField(max_length=-1)
    bowel_sounds = models.CharField(max_length=-1)
    dialysis = models.BooleanField()
    chest_expansion = models.CharField(max_length=-1)
    xray = models.TextField() # This field type is a guess.
    bacteremia = models.BooleanField()
    gcs = models.ForeignKey(GnuhealthIcuGlasgow, db_column='gcs')
    anisocoria = models.BooleanField()
    left_pupil = models.IntegerField()
    ecg = models.ForeignKey(GnuhealthIcuEcg, db_column='ecg')
    venous_access = models.CharField(max_length=-1)
    pupil_consensual_resp = models.BooleanField()
    stools = models.CharField(max_length=-1)
    paradoxical_expansion = models.BooleanField()
    cellulitis = models.BooleanField()
    ssi = models.BooleanField()
    arterial_access = models.BooleanField()
    peep = models.BooleanField()
    vomiting = models.CharField(max_length=-1)
    respiration_type = models.CharField(max_length=-1)
    oxygen_mask = models.BooleanField()
    necrotizing_fasciitis = models.BooleanField()
    swan_ganz = models.BooleanField()
    oral_mucosa_lesion = models.BooleanField()
    wound_dehiscence = models.BooleanField()
    peritonitis = models.BooleanField()
    trachea_alignment = models.CharField(max_length=-1)
    icu_patient = models.BooleanField()
    tracheal_tug = models.BooleanField()
    peep_pressure = models.IntegerField()
    pupil_dilation = models.CharField(max_length=-1)
    right_pupil = models.IntegerField()
    hospitalization_location = models.ForeignKey(StockLocation, db_column='hospitalization_location')
    state = models.CharField(max_length=-1)
    class Meta:
        db_table = u'gnuhealth_patient_rounding'

class GnuhealthPatientRoundingVaccine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.ForeignKey(GnuhealthPatientRounding, db_column='name')
    short_comment = models.CharField(max_length=-1)
    dose = models.IntegerField()
    vaccine = models.ForeignKey(ProductProduct, db_column='vaccine')
    lot = models.ForeignKey(StockLot, db_column='lot')
    next_dose_date = models.DateTimeField()
    quantity = models.IntegerField()
    class Meta:
        db_table = u'gnuhealth_patient_rounding_vaccine'

class StockPeriod(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    state = models.CharField(max_length=-1)
    date = models.DateField()
    class Meta:
        db_table = u'stock_period'

class StockPeriodCache(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    internal_quantity = models.FloatField()
    product = models.ForeignKey(ProductProduct, db_column='product')
    period = models.ForeignKey(StockPeriod, db_column='period')
    location = models.ForeignKey(StockLocation, db_column='location')
    class Meta:
        db_table = u'stock_period_cache'

class StockShipmentInternal(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1)
    from_location = models.ForeignKey(StockLocation, db_column='from_location')
    planned_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    state = models.CharField(max_length=-1)
    to_location = models.ForeignKey(StockLocation, db_column='to_location')
    effective_date = models.DateField()
    class Meta:
        db_table = u'stock_shipment_internal'

class StockShipmentInReturn(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1)
    from_location = models.ForeignKey(StockLocation, db_column='from_location')
    planned_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    state = models.CharField(max_length=-1)
    to_location = models.ForeignKey(StockLocation, db_column='to_location')
    effective_date = models.DateField()
    class Meta:
        db_table = u'stock_shipment_in_return'

class StockShipmentOut(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    customer = models.ForeignKey(PartyParty, db_column='customer')
    code = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1)
    delivery_address = models.ForeignKey(PartyAddress, db_column='delivery_address')
    planned_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    warehouse = models.ForeignKey(StockLocation, db_column='warehouse')
    state = models.CharField(max_length=-1)
    effective_date = models.DateField()
    prescription_order = models.ForeignKey(GnuhealthPrescriptionOrder, db_column='prescription_order')
    class Meta:
        db_table = u'stock_shipment_out'

class StockShipmentOutReturn(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    customer = models.ForeignKey(PartyParty, db_column='customer')
    code = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1)
    delivery_address = models.ForeignKey(PartyAddress, db_column='delivery_address')
    planned_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    warehouse = models.ForeignKey(StockLocation, db_column='warehouse')
    state = models.CharField(max_length=-1)
    effective_date = models.DateField()
    class Meta:
        db_table = u'stock_shipment_out_return'

class StockShipmentIn(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    planned_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    supplier = models.ForeignKey(PartyParty, db_column='supplier')
    contact_address = models.ForeignKey(PartyAddress, db_column='contact_address')
    warehouse = models.ForeignKey(StockLocation, db_column='warehouse')
    effective_date = models.DateField()
    class Meta:
        db_table = u'stock_shipment_in'

class CompanyCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    parent = models.ForeignKey('self', db_column='parent')
    footer = models.TextField()
    header = models.TextField()
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    party = models.ForeignKey(PartyParty, db_column='party')
    class Meta:
        db_table = u'company_company'

class StockLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    input_location = models.ForeignKey('self', db_column='input_location')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    output_location = models.ForeignKey('self', db_column='output_location')
    right = models.IntegerField()
    address = models.ForeignKey(PartyAddress, db_column='address')
    active = models.BooleanField()
    left = models.IntegerField()
    type = models.CharField(max_length=-1)
    storage_location = models.ForeignKey('self', db_column='storage_location')
    class Meta:
        db_table = u'stock_location'

class StockMove(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    planned_date = models.DateField()
    currency = models.ForeignKey(CurrencyCurrency, db_column='currency')
    shipment_internal = models.ForeignKey(StockShipmentInternal, db_column='shipment_internal')
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    state = models.CharField(max_length=-1)
    effective_date = models.DateField()
    shipment_in_return = models.ForeignKey(StockShipmentInReturn, db_column='shipment_in_return')
    uom = models.ForeignKey(ProductUom, db_column='uom')
    cost_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    internal_quantity = models.FloatField()
    product = models.ForeignKey(ProductProduct, db_column='product')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    shipment_out_return = models.ForeignKey(StockShipmentOutReturn, db_column='shipment_out_return')
    to_location = models.ForeignKey(StockLocation, db_column='to_location')
    from_location = models.ForeignKey(StockLocation, db_column='from_location')
    shipment_out = models.ForeignKey(StockShipmentOut, db_column='shipment_out')
    shipment_in = models.ForeignKey(StockShipmentIn, db_column='shipment_in')
    quantity = models.FloatField()
    lot = models.ForeignKey(StockLot, db_column='lot')
    ambulatory_care = models.ForeignKey(GnuhealthPatientAmbulatoryCare, db_column='ambulatory_care')
    rounding = models.ForeignKey(GnuhealthPatientRounding, db_column='rounding')
    class Meta:
        db_table = u'stock_move'

class StockInventory(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    state = models.CharField(max_length=-1)
    location = models.ForeignKey(StockLocation, db_column='location')
    date = models.DateField()
    lost_found = models.ForeignKey(StockLocation, db_column='lost_found')
    class Meta:
        db_table = u'stock_inventory'

class StockInventoryLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    product = models.ForeignKey(ProductProduct, db_column='product')
    move = models.ForeignKey(StockMove, db_column='move')
    expected_quantity = models.FloatField()
    inventory = models.ForeignKey(StockInventory, db_column='inventory')
    quantity = models.FloatField()
    class Meta:
        db_table = u'stock_inventory_line'

class ProductProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    description = models.TextField()
    template = models.ForeignKey(ProductTemplate, db_column='template')
    is_bed = models.BooleanField()
    is_insurance_plan = models.BooleanField()
    is_vaccine = models.BooleanField()
    is_medicament = models.BooleanField()
    class Meta:
        db_table = u'product_product'

class StockConfiguration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'stock_configuration'

class AccountAccountTypeTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    sequence = models.IntegerField()
    balance_sheet = models.BooleanField()
    display_balance = models.CharField(max_length=-1)
    income_statement = models.BooleanField()
    class Meta:
        db_table = u'account_account_type_template'

class AccountAccountType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    sequence = models.IntegerField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    balance_sheet = models.BooleanField()
    display_balance = models.CharField(max_length=-1)
    template = models.ForeignKey(AccountAccountTypeTemplate, db_column='template')
    income_statement = models.BooleanField()
    class Meta:
        db_table = u'account_account_type'

class AccountAccountDeferral(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccount, db_column='account')
    credit = models.DecimalField(max_digits=65535, decimal_places=65535)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535)
    fiscalyear = models.ForeignKey(AccountFiscalyear, db_column='fiscalyear')
    class Meta:
        db_table = u'account_account_deferral'

class AccountConfiguration(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    class Meta:
        db_table = u'account_configuration'

class AccountJournalType(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(unique=True, max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_journal_type'

class AccountJournalViewColumn(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    required = models.BooleanField()
    field = models.ForeignKey(IrModelField, db_column='field')
    readonly = models.BooleanField()
    view = models.ForeignKey(AccountJournalView, db_column='view')
    class Meta:
        db_table = u'account_journal_view_column'

class AccountJournalView(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_journal_view'

class AccountJournal(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    update_posted = models.BooleanField()
    code = models.CharField(max_length=-1)
    view = models.ForeignKey(AccountJournalView, db_column='view')
    active = models.BooleanField()
    centralised = models.BooleanField()
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_journal'

class AccountJournalPeriod(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, db_column='journal')
    period = models.ForeignKey(AccountPeriod, db_column='period')
    state = models.CharField(max_length=-1)
    active = models.BooleanField()
    class Meta:
        db_table = u'account_journal_period'

class AccountPeriod(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    end_date = models.DateField()
    post_move_sequence = models.ForeignKey(IrSequence, db_column='post_move_sequence')
    start_date = models.DateField()
    state = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    fiscalyear = models.ForeignKey(AccountFiscalyear, db_column='fiscalyear')
    out_invoice_sequence = models.ForeignKey(IrSequenceStrict, db_column='out_invoice_sequence')
    in_credit_note_sequence = models.ForeignKey(IrSequenceStrict, db_column='in_credit_note_sequence')
    in_invoice_sequence = models.ForeignKey(IrSequenceStrict, db_column='in_invoice_sequence')
    out_credit_note_sequence = models.ForeignKey(IrSequenceStrict, db_column='out_credit_note_sequence')
    class Meta:
        db_table = u'account_period'

class AccountMoveReconciliation(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_move_reconciliation'

class AccountMove(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    origin = models.CharField(max_length=-1)
    description = models.CharField(max_length=-1)
    post_number = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, db_column='journal')
    number = models.CharField(max_length=-1)
    period = models.ForeignKey(AccountPeriod, db_column='period')
    post_date = models.DateField()
    state = models.CharField(max_length=-1)
    date = models.DateField()
    centralised_line = models.ForeignKey(AccountMoveLine, db_column='centralised_line')
    class Meta:
        db_table = u'account_move'

class AccountFiscalyear(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    end_date = models.DateField()
    company = models.ForeignKey(CompanyCompany, db_column='company')
    post_move_sequence = models.ForeignKey(IrSequence, db_column='post_move_sequence')
    start_date = models.DateField()
    state = models.CharField(max_length=-1)
    out_invoice_sequence = models.ForeignKey(IrSequenceStrict, db_column='out_invoice_sequence')
    in_credit_note_sequence = models.ForeignKey(IrSequenceStrict, db_column='in_credit_note_sequence')
    in_invoice_sequence = models.ForeignKey(IrSequenceStrict, db_column='in_invoice_sequence')
    out_credit_note_sequence = models.ForeignKey(IrSequenceStrict, db_column='out_credit_note_sequence')
    class Meta:
        db_table = u'account_fiscalyear'

class AccountFiscalyearLineRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    line = models.ForeignKey(AccountMoveLine, db_column='line')
    fiscalyear = models.ForeignKey(AccountFiscalyear, db_column='fiscalyear')
    class Meta:
        db_table = u'account_fiscalyear_line_rel'

class AccountTaxCodeTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccountTemplate, db_column='account')
    code = models.CharField(max_length=-1)
    description = models.TextField()
    parent = models.ForeignKey('self', db_column='parent')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_tax_code_template'

class AccountMoveLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    move = models.ForeignKey(AccountMove, db_column='move')
    amount_second_currency = models.DecimalField(max_digits=65535, decimal_places=65535)
    state = models.CharField(max_length=-1)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535)
    party = models.ForeignKey(PartyParty, db_column='party')
    description = models.CharField(max_length=-1)
    reconciliation = models.ForeignKey(AccountMoveReconciliation, db_column='reconciliation')
    second_currency = models.ForeignKey(CurrencyCurrency, db_column='second_currency')
    account = models.ForeignKey(AccountAccount, db_column='account')
    maturity_date = models.DateField()
    credit = models.DecimalField(max_digits=65535, decimal_places=65535)
    class Meta:
        db_table = u'account_move_line'

class AccountTaxCode(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    description = models.TextField()
    parent = models.ForeignKey('self', db_column='parent')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    code = models.CharField(max_length=-1)
    template = models.ForeignKey(AccountTaxCodeTemplate, db_column='template')
    active = models.BooleanField()
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_tax_code'

class AccountTaxLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.ForeignKey(AccountTaxCode, db_column='code')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    move_line = models.ForeignKey(AccountMoveLine, db_column='move_line')
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    class Meta:
        db_table = u'account_tax_line'

class AccountTaxRuleTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccountTemplate, db_column='account')
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_tax_rule_template'

class AccountTaxRule(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    name = models.CharField(max_length=-1)
    company = models.ForeignKey(CompanyCompany, db_column='company')
    template = models.ForeignKey(AccountTaxRuleTemplate, db_column='template')
    class Meta:
        db_table = u'account_tax_rule'

class AccountTaxRuleLineTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    tax = models.ForeignKey(AccountTaxTemplate, db_column='tax')
    rule = models.ForeignKey(AccountTaxRuleTemplate, db_column='rule')
    group = models.ForeignKey(AccountTaxGroup, db_column='group')
    origin_tax = models.ForeignKey(AccountTaxTemplate, db_column='origin_tax')
    class Meta:
        db_table = u'account_tax_rule_line_template'

class AccountTaxGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    class Meta:
        db_table = u'account_tax_group'

class AccountTaxRuleLine(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    tax = models.ForeignKey(AccountTax, db_column='tax')
    rule = models.ForeignKey(AccountTaxRule, db_column='rule')
    template = models.ForeignKey(AccountTaxRuleLineTemplate, db_column='template')
    group = models.ForeignKey(AccountTaxGroup, db_column='group')
    origin_tax = models.ForeignKey(AccountTax, db_column='origin_tax')
    class Meta:
        db_table = u'account_tax_rule_line'

class AccountAccountTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    kind = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    deferral = models.BooleanField()
    type = models.ForeignKey(AccountAccountTypeTemplate, db_column='type')
    reconcile = models.BooleanField()
    class Meta:
        db_table = u'account_account_template'

class AccountTaxTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    invoice_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    credit_note_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(AccountTaxGroup, db_column='group')
    invoice_account = models.ForeignKey(AccountAccountTemplate, db_column='invoice_account')
    credit_note_tax_code = models.ForeignKey(AccountTaxCodeTemplate, db_column='credit_note_tax_code')
    percentage = models.DecimalField(max_digits=65535, decimal_places=65535)
    type = models.CharField(max_length=-1)
    description = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    invoice_tax_code = models.ForeignKey(AccountTaxCodeTemplate, db_column='invoice_tax_code')
    invoice_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    credit_note_account = models.ForeignKey(AccountAccountTemplate, db_column='credit_note_account')
    account = models.ForeignKey(AccountAccountTemplate, db_column='account')
    name = models.CharField(max_length=-1)
    credit_note_base_code = models.ForeignKey(AccountTaxCodeTemplate, db_column='credit_note_base_code')
    credit_note_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    invoice_base_code = models.ForeignKey(AccountTaxCodeTemplate, db_column='invoice_base_code')
    class Meta:
        db_table = u'account_tax_template'

class AccountAccountTemplateTaxRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccountTemplate, db_column='account')
    tax = models.ForeignKey(AccountTaxTemplate, db_column='tax')
    class Meta:
        db_table = u'account_account_template_tax_rel'

class AccountAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    reconcile = models.BooleanField()
    code = models.CharField(max_length=-1)
    right = models.IntegerField()
    note = models.TextField()
    template = models.ForeignKey(AccountAccountTemplate, db_column='template')
    type = models.ForeignKey(AccountAccountType, db_column='type')
    parent = models.ForeignKey('self', db_column='parent')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    active = models.BooleanField()
    second_currency = models.ForeignKey(CurrencyCurrency, db_column='second_currency')
    kind = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    deferral = models.BooleanField()
    left = models.IntegerField()
    class Meta:
        db_table = u'account_account'

class AccountAccountTaxRel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    account = models.ForeignKey(AccountAccount, db_column='account')
    tax = models.ForeignKey(AccountTax, db_column='tax')
    class Meta:
        db_table = u'account_account_tax_rel'

class AccountTax(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    create_uid = models.ForeignKey(ResUser, db_column='create_uid')
    write_uid = models.ForeignKey(ResUser, db_column='write_uid')
    sequence = models.IntegerField()
    invoice_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    credit_note_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(AccountTaxGroup, db_column='group')
    invoice_account = models.ForeignKey(AccountAccount, db_column='invoice_account')
    credit_note_tax_code = models.ForeignKey(AccountTaxCode, db_column='credit_note_tax_code')
    template = models.ForeignKey(AccountTaxTemplate, db_column='template')
    percentage = models.DecimalField(max_digits=65535, decimal_places=65535)
    type = models.CharField(max_length=-1)
    description = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', db_column='parent')
    company = models.ForeignKey(CompanyCompany, db_column='company')
    invoice_tax_code = models.ForeignKey(AccountTaxCode, db_column='invoice_tax_code')
    active = models.BooleanField()
    invoice_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    credit_note_account = models.ForeignKey(AccountAccount, db_column='credit_note_account')
    name = models.CharField(max_length=-1)
    credit_note_base_code = models.ForeignKey(AccountTaxCode, db_column='credit_note_base_code')
    credit_note_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    invoice_base_code = models.ForeignKey(AccountTaxCode, db_column='invoice_base_code')
    class Meta:
        db_table = u'account_tax'


