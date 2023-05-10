# E-RIHS Controlled Lists

The various controlled lists presented here are being used within the development of documentation and data gathering exercises, in relation to Heritage Science research activities. This standard metadata modelling and data gathering work is being carried out within [IPERION-HS](https://cordis.europa.eu/project/id/871034) and [E-RIHS IP](https://cordis.europa.eu/project/id/101079148) as part of the development of [E-RIHS](https://www.e-rihs.eu/). 

> **Note**
>
> It is planned that once the process of creation and editing of these controlled lists reaches a more robust and consistent level the various lists and their administration will be moved to a feature rich vocabulary service. which is currently expected to be hosted under https://vocabulary.e-rihs.io (this is not yet live).

The controlled lists added to this repository are being managed and created using a very fixed file and folder name protocol. This allows the lists content to be created and edited via simple TSV files and then more functional JSON formatted representations are created automatically by an in built GitHub Actions script that calls the included [tsv2json](scripts/tsv2json.py) script.

**Please only edit the files within the tsv folder as indicated below**

## Contributions

* Each of the controlled lists are created or edited via the folders and files listed below the [tsv](tsv) folder.
* To create a new controlled list:
  - step 1
  - step 2
  
## List Format
 
The terms included within this list should be saved within Tab Separated Value (TSV) files within this folder with the following structure:
 
|DB Term |Display Name | Term Description | Same As | Source |
| ------------- |:-------------:| -----:| -----:| -----:|
| term_id_1 | Display Name 1 | Description 1 | Same As URL 1 | - |
| term_id_2 | Display Name 2 | Description 2 | - | Source URL 2 |
 
* **term_id**: name_formatted_as_an_id 
* **Display Name**: _(language specific)_ Indicate how the term should appear when actually displayed in a drop-down list or related form.
**Description**: _(language specific)_ A short free text description of what the term means - this field can be left blank for terms that have a direct Same As URL that already contains a full description of the term. (An existing description can be copied in, but please cite the source)
* **Same As URL**: _(optional where appropriate)_ Where a term is directly taken or can be directly referenced to and exiting standard term, for example from [AAT](https://www.getty.edu/research/tools/vocabularies/aat/) or [Wikidata](https://www.wikidata.org/) include the URL for that term. 
* **Source URL**: _(optional where appropriate)_ If a term is not a direct version of an existing term, but is related to or is a derivative of an existing term/process/method include an appropriate URL.

### List Language

The default language of these controlled lists is expected to be English but alternative languages files can also be save here. the TSV files should be named as shown here:
* controlled_list_tag_LanguageCode.tsv
* For example: **service_readiness_level_en.tsv**

## Current Lists
* service_readiness_level
* natural_languages
* support_activity_type

## Planned Lists
* service_technique
* service_platform
* offered_to
* national_node
* research_disciplines
* service_categories
* service_functions
* service_link_type
* service_keywords - needs to be treated differently - example list
* service_access_unit
* Research Category
* project state
* participant role
* examination type (object/Archive/Data)
* Technique
* Condition Class/State/Value (Possibly several lists see model notes)
* Actor Type
