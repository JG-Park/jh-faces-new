from django.db import models
class ResultGEO(models.Model):
    unnamed_0 = models.IntegerField()
    fid = models.IntegerField()
    gid = models.CharField(max_length=255, primary_key=True)
    emd_cd = models.IntegerField()
    emd_nm_k = models.CharField(max_length=255)
    charging_station_accessibility = models.FloatField()
    gas_station_count = models.IntegerField()
    charging_station_count = models.IntegerField()
    performance_facility_accessibility = models.FloatField()
    public_price = models.FloatField()
    library_accessibility = models.FloatField()
    hospital_accessibility = models.FloatField()
    health_center_accessibility = models.FloatField()
    community_park_accessibility = models.FloatField()
    fire_station_accessibility = models.FloatField()
    population = models.IntegerField()
    theme_park_accessibility = models.FloatField()
    parking_lot_accessibility = models.FloatField()
    sports_facility_accessibility = models.FloatField()
    elementary_school_accessibility = models.FloatField()
    fast_charging = models.IntegerField()
    agricultural_area = models.IntegerField()
    altitude = models.IntegerField()
    river = models.IntegerField()
    center_coordinates = models.CharField(max_length=255)
    y_pred_rf = models.IntegerField()
    y_pred_lgb = models.IntegerField()
    y_pred_xgb = models.IntegerField()
    y_pred_voting = models.IntegerField()
    cluster_id = models.IntegerField()
    cluster_size = models.IntegerField()
    coordinates = models.JSONField()

class RecommandGEO(models.Model):
    unnamed_0 = models.IntegerField(blank=True, null=True)  # 기본키로 사용되지 않으므로 null 허용으로 변경
    fid = models.IntegerField(blank=True, null=True)  # 필수가 아니라면 null 허용으로 변경
    gid = models.CharField(max_length=255, primary_key=True)
    emd_cd = models.IntegerField()
    emd_nm_k = models.CharField(max_length=255)
    charging_station_accessibility = models.FloatField(null=True)
    gas_station_count = models.IntegerField(null=True)
    charging_station_count = models.IntegerField(null=True)
    performance_facility_accessibility = models.FloatField(null=True)
    public_price = models.FloatField(null=True)
    library_accessibility = models.FloatField(null=True)
    hospital_accessibility = models.FloatField(null=True)
    health_center_accessibility = models.FloatField(null=True)
    community_park_accessibility = models.FloatField(null=True)
    fire_station_accessibility = models.FloatField(null=True)
    population = models.IntegerField(null=True)
    theme_park_accessibility = models.FloatField(null=True)
    parking_lot_accessibility = models.FloatField(null=True)
    sports_facility_accessibility = models.FloatField(null=True)
    elementary_school_accessibility = models.FloatField(null=True)
    fast_charging = models.IntegerField(null=True)
    agricultural_area = models.IntegerField(null=True)
    altitude = models.IntegerField(null=True)
    river = models.IntegerField(null=True)
    center_coordinates = models.CharField(max_length=255, null=True)
    y_pred_rf = models.IntegerField(null=True)
    y_pred_lgb = models.IntegerField(null=True)
    y_pred_xgb = models.IntegerField(null=True)
    y_pred_voting = models.IntegerField(null=True)
    cluster_id = models.IntegerField(null=True)
    cluster_size = models.IntegerField(null=True)
    coordinates = models.JSONField(null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    detailed_category = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.IntegerField(blank=True, null=True)
    road_name_code = models.IntegerField(blank=True, null=True)
    road_address = models.CharField(max_length=255, blank=True, null=True)
    institution_name = models.CharField(max_length=255, blank=True, null=True)
    position_x = models.FloatField(blank=True, null=True)
    position_y = models.FloatField(blank=True, null=True)

class RecommandGSGEO(models.Model):
    unnamed_0 = models.IntegerField(blank=True, null=True)
    fid = models.IntegerField()
    gid = models.CharField(max_length=255, primary_key=True)
    emd_cd = models.IntegerField()
    emd_nm_k = models.CharField(max_length=255)
    charging_station_accessibility = models.FloatField()
    gas_station_count = models.IntegerField()
    charging_station_count = models.IntegerField()
    performance_facility_accessibility = models.FloatField()
    public_price = models.FloatField()
    library_accessibility = models.FloatField()
    hospital_accessibility = models.FloatField()
    health_center_accessibility = models.FloatField()
    community_park_accessibility = models.FloatField()
    fire_station_accessibility = models.FloatField()
    population = models.IntegerField()
    theme_park_accessibility = models.FloatField()
    parking_lot_accessibility = models.FloatField()
    sports_facility_accessibility = models.FloatField()
    elementary_school_accessibility = models.FloatField()
    fast_charging = models.IntegerField()
    agricultural_area = models.IntegerField()
    altitude = models.IntegerField()
    river = models.IntegerField()
    center_coordinates = models.CharField(max_length=255)
    y_pred_rf = models.IntegerField()
    y_pred_lgb = models.IntegerField()
    y_pred_xgb = models.IntegerField()
    y_pred_voting = models.IntegerField()
    cluster_id = models.IntegerField()
    cluster_size = models.IntegerField()
    gas_station_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="주유소/충전소명")
    address_jibun = models.CharField(max_length=255, blank=True, null=True, verbose_name="소재지지번주소")
    longitude = models.FloatField(blank=True, null=True, verbose_name="경도")
    latitude = models.FloatField(blank=True, null=True, verbose_name="위도")


class existInstalledGEO(models.Model):
    unnamed_0 = models.IntegerField(blank=True, null=True)
    installation_year = models.IntegerField(verbose_name="설치년도")
    address = models.CharField(max_length=255, verbose_name="주소")
    charging_station_name = models.CharField(max_length=255, verbose_name="충전소명")
    facility_category_major = models.CharField(max_length=255, verbose_name="시설구분(대)")
    facility_category_minor = models.CharField(max_length=255, verbose_name="시설구분(소)")
    model_type_major = models.CharField(max_length=255, verbose_name="기종(대)")
    model_type_minor = models.CharField(max_length=255, verbose_name="기종(소)")
    operating_org_major = models.CharField(max_length=255, verbose_name="운영기관(대)")
    operating_org_minor = models.CharField(max_length=255, verbose_name="운영기관(소)")
    charger_type = models.CharField(max_length=255, verbose_name="충전기타입")
    user_restriction = models.CharField(max_length=255, verbose_name="이용자제한")
    charger_id = models.IntegerField(verbose_name="충전기ID")
    charging_station_id = models.CharField(max_length=255, verbose_name="충전소ID")
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    fid = models.IntegerField(blank=True, null=True)
    gid = models.CharField(max_length=255, primary_key=True)
    emd_cd = models.IntegerField(verbose_name="emd_cd")
    emd_nm_k = models.CharField(max_length=255, verbose_name="emd_nm_k")
    charging_station_accessibility = models.FloatField(verbose_name="충전소접근성")
    gas_station_count = models.IntegerField(verbose_name="주유소_수")
    charging_station_count = models.IntegerField(verbose_name="충전소_수")
    performance_facility_accessibility = models.FloatField(verbose_name="공연시설접근성")
    public_price = models.FloatField(verbose_name="공시지가")
    library_accessibility = models.FloatField(verbose_name="도서관접근성")
    hospital_accessibility = models.FloatField(verbose_name="병원접근성")
    health_center_accessibility = models.FloatField(verbose_name="보건기관접근성")
    community_park_accessibility = models.FloatField(verbose_name="생활권공원접근성")
    fire_station_accessibility = models.FloatField(verbose_name="소방서접근성")
    population = models.IntegerField(verbose_name="인구")
    theme_park_accessibility = models.FloatField(verbose_name="주제공원접근성")
    parking_lot_accessibility = models.FloatField(verbose_name="주차장접근성")
    sports_facility_accessibility = models.FloatField(verbose_name="체육시설접근성")
    elementary_school_accessibility = models.FloatField(verbose_name="초등학교접근성")
    fast_charging = models.IntegerField(verbose_name="급/완속여부")
    agricultural_area = models.IntegerField(verbose_name="농림지역")
    altitude = models.IntegerField(verbose_name="고도")
    river = models.IntegerField(verbose_name="하천")
    center_coordinates = models.CharField(max_length=255, verbose_name="중심좌표")
    y_pred_rf = models.IntegerField(blank=True, null=True)
    y_pred_lgb = models.IntegerField(blank=True, null=True)
    y_pred_xgb = models.IntegerField(blank=True, null=True)
    y_pred_voting = models.IntegerField(blank=True, null=True)
    cluster_id = models.IntegerField(blank=True, null=True)
    cluster_size = models.IntegerField(blank=True, null=True)
    coordinates = models.JSONField()



class existInstalledGridGEO(models.Model):
    unnamed_0 = models.IntegerField(blank=True, null=True)
    fid = models.IntegerField()
    gid = models.CharField(max_length=255, primary_key=True)
    emd_cd = models.IntegerField()
    emd_nm_k = models.CharField(max_length=255)
    charging_station_accessibility = models.FloatField()
    gas_station_count = models.IntegerField()
    charging_station_count = models.IntegerField()
    performance_facility_accessibility = models.FloatField()
    public_price = models.FloatField()
    library_accessibility = models.FloatField()
    hospital_accessibility = models.FloatField()
    health_center_accessibility = models.FloatField()
    community_park_accessibility = models.FloatField()
    fire_station_accessibility = models.FloatField()
    population = models.FloatField()
    theme_park_accessibility = models.FloatField()
    parking_lot_accessibility = models.FloatField()
    sports_facility_accessibility = models.FloatField()
    elementary_school_accessibility = models.FloatField()
    fast_charging = models.IntegerField()
    agricultural_area = models.IntegerField()
    average_altitude = models.IntegerField()  # "평균고도" 필드 추가
    river = models.IntegerField()
    center_coordinates = models.CharField(max_length=255)
    # Polygon 정보를 저장하기 위해 GeoDjango의 PolygonField를 사용
    coordinates = models.JSONField()