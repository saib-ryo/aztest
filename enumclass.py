import enum

#プロジェクト達成度のクラス
@enum.unique
class ProjectAchievement(enum.Enum):
    concept_proposal = 1
    idea_of_method = 2
    analysis_design = 3
    trial = 4
    demonstration = 5
    comitt = 6
    @property
    def view_name(self) -> str:
        return {
            ProjectAchievement.concept_proposal: "コンセプト提案",
            ProjectAchievement.idea_of_method: "手法の考案",
            ProjectAchievement.analysis_design: "解析・設計",
            ProjectAchievement.trial: "試行・試作",
            ProjectAchievement.demonstration: "実証・検証（製品化直前）",
            ProjectAchievement.comitt: "完了（実用化）"
        }[self]


#社会実装のクラス
@enum.unique
class SocialImplementation(enum.Enum):
    social_implementation_type_joint_research = 1
    other_joint_research = 2
    independent_research = 3
    @property
    def view_name(self) -> str:
        return {
            SocialImplementation.social_implementation_type_joint_research: "社会実装型共同研究",
            SocialImplementation.other_joint_research: "その他共同研究",
            SocialImplementation.independent_research: "単独研究",
        }[self]


#社会実装パートナー(共同研究)
@enum.unique
class ResearchPartners(enum.Enum):
    parties = 1
    special_education_school = 2
    hospital_medical_institution = 3
    welfare_facility = 4
    companies_organizations = 5
    university_educational_institutions = 6
    other = 99
    @property
    def view_name(self) -> str:
        return {
            ResearchPartners.parties: "当事者",
            ResearchPartners.special_education_school: "特別支援学校",
            ResearchPartners.hospital_medical_institution: "病院・医療機関",
            ResearchPartners.welfare_facility: "福祉施設",
            ResearchPartners.companies_organizations: "企業・団体",
            ResearchPartners.university_educational_institutions: "大学等の教育機関",
            ResearchPartners.other: "その他",
        }[self]


#支援分類
@enum.unique
class SupportCategory(enum.Enum):
    support_for_the_disabled = 1
    support_for_the_elderly = 2
    medical_and_industrial_cooperation = 3
    agricultural_and_industrial_cooperation = 4
    other = 99
    @property
    def view_name(self) -> str:
        return {
            SupportCategory.support_for_the_disabled: "障害者支援",
            SupportCategory.support_for_the_elderly: "高齢者支援",
            SupportCategory.medical_and_industrial_cooperation: "医工連携",
            SupportCategory.agricultural_and_industrial_cooperation: "農工連携",
            SupportCategory.other: "その他",
        }[self]


#支援対象
@enum.unique
class SupportCategoryTarget(enum.Enum):
    support_for_the_physically_handicapped = 1
    support_for_the_visually_impaired = 2
    support_for_the_hearing_impaired = 3
    support_for_the_mentally_disabled = 4
    support_for_people_with_multiple_disabilities = 5
    cooperative_person_support = 6
    medical_support = 7
    other = 99
    @property
    def view_name(self) -> str:
        return {
            SupportCategoryTarget.support_for_the_physically_handicapped: "肢体不自由者支援",
            SupportCategoryTarget.support_for_the_visually_impaired: "視覚障害者支援",
            SupportCategoryTarget.support_for_the_hearing_impaired: "聴覚障害者支援",
            SupportCategoryTarget.support_for_the_mentally_disabled: "知的障害者支援",
            SupportCategoryTarget.support_for_people_with_multiple_disabilities: "重複障害者支援",
            SupportCategoryTarget.cooperative_person_support: "協力（支援）者支援",
            SupportCategoryTarget.medical_support: "医用支援",
            SupportCategoryTarget.other: "その他"
        }[self]


#支援内容
@enum.unique
class SupportCategoryContents(enum.Enum):
    behavioral_support = 1
    rehabilitation = 2
    work_and_labor_support = 3
    watching_over = 4
    therapeutic_support = 5
    mobility_support =6 
    motion_support = 7
    operation_support = 8
    learning_support = 9
    diagnostic_support = 10
    other = 99
    @property
    def view_name(self) -> str:
        return {
            SupportCategoryContents.behavioral_support: "生活行動支援",
            SupportCategoryContents.rehabilitation: "リハビリテーション",
            SupportCategoryContents.work_and_labor_support: "作業労働支援",
            SupportCategoryContents.watching_over: "見守り",
            SupportCategoryContents.therapeutic_support: "治療支援",
            SupportCategoryContents.mobility_support: "移動支援",
            SupportCategoryContents.motion_support: "動作支援",
            SupportCategoryContents.operation_support: "操作支援",
            SupportCategoryContents.learning_support: "学習支援",
            SupportCategoryContents.diagnostic_support: "診断支援",
            SupportCategoryContents.other: "その他"
        }[self]


#分野
@enum.unique
class FieldCategory(enum.Enum):
    electronic_circuits = 1
    sensors_devices = 2
    machine_learning_machine_elements = 3
    architecture_environmental_design = 4
    robotics_mechatronics = 5
    programming = 6
    experiment = 7
    other = 99
    @property
    def view_name(self) -> str:
        return {
            FieldCategory.electronic_circuits: "電気・電子回路",
            FieldCategory.sensors_devices: "センサ/デバイス",
            FieldCategory.machine_learning_machine_elements: "機械学習・機械要素",
            FieldCategory.architecture_environmental_design: "建築・環境デザイン",
            FieldCategory.robotics_mechatronics: "ロボット/メカトロニクス",
            FieldCategory.programming: "プログラミング",
            FieldCategory.experiment: "実験・計測・測定",
            FieldCategory.other: "その他",
        }[self]


#分野（ソフトウェア）
@enum.unique
class FieldCategorySoftware(enum.Enum):
    pc_software = 1 
    mobile_apps = 2
    web_services = 3
    algorithm = 4
    image_processing = 5
    speech_information_processing = 6
    AI_applications = 7
    other = 99
    @property
    def view_name(self) -> str:
        return {
            FieldCategorySoftware.electronic_circuits: "電気・電子回路",
            FieldCategorySoftware.pc_software: "PCソフトウェア",
            FieldCategorySoftware.mobile_apps: "スマホ/モバイルアプリ",
            FieldCategorySoftware.web_services: "Webサービス",
            FieldCategorySoftware.algorithm: "アルゴリズム",
            FieldCategorySoftware.image_processing: "画像処理",
            FieldCategorySoftware.speech_information_processing: "音声情報処理",
            FieldCategorySoftware.AI_applications: "AI応用",
            FieldCategorySoftware.other: "その他"
        }[self]


#分野（デバイス）
@enum.unique
class FieldCategoryDevice(enum.Enum):
    pc_tablet_use = 1
    Using_Rapberry_PI = 2
    Using_Arduino = 3
    Using_DSP_board = 4
    Using_other_microcomputers = 5
    ROS_application =6
    other = 99
    @property
    def view_name(self) -> str:
        return {
            FieldCategoryDevice.pc_tablet_use: "PC/タブレット使用",
            FieldCategoryDevice.Using_Rapberry_PI: "Rapberry PI利用",
            FieldCategoryDevice.Using_Arduino: "Arduino利用",
            FieldCategoryDevice.Using_DSP_board: "DSPボード利用",
            FieldCategoryDevice.Using_other_microcomputers: "その他マイコン利用",
            FieldCategoryDevice.ROS_application: "その他マイコン利用",
            FieldCategoryDevice.other: "その他"
        }[self]