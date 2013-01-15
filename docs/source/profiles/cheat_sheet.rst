AGX cheat sheet
================

.. list-table:: **List of Profiles and Stereotypes**
   :widths: 10 35 10 45
   :header-rows: 1

   * - Profile
     - UML:Stereotype
     - Metaclasses
     - Tagged Values
   * - the profile 
     - name of stereotype with link to details
     - applicable to
     - see link for description
   * - **pyegg**
     - .
     - .
     - .
   * - ''
     - :ref:`st_pyegg`
     - UML:Package
     - version, description, authors, email, keywords, url, license,
       zipsafe, classifiers, copyrights
   * - .
     - :ref:`st_pypackage`
     - UML:Package
     - None
   * - .
     - :ref:`st_pymodule`
     - UML:Package
     - None
   * - .
     - :ref:`st_stub`
     - UML:Interface, UML:Class
     - import
   * - ''
     - :ref:`st_api`
     - UML:Class
     - None
   * - ''
     - :ref:`st_function`
     - UML:Class, UML:Operation
     - args, kwargs
   * - ''
     - :ref:`st_decorator`
     - UML:Class, UML:Operation
     - name, args, kwargs
   * - ''
     - :ref:`st_derive`
     - UML:Generalization
     - order
   * - ''
     - :ref:`st_expression`
     - UML:Property
     - expression
   * - **buildout**
     - .
     - .
     - .
   * - ''
     - :ref:`st_plone_self_contained`
     - UML:Package
     - None
   * - **zca**
     - .
     - .
     - .
   * - ''
     - :ref:`st_permission`
     - UML:Package
     - --
   * - ''
     - :ref:`st_subscriber`
     - UML:Class
     - title, description, id
   * - ''
     - :ref:`st_adapter`
     - UML:Class, UML:Interface
     - name
   * - ''
     - :ref:`st_utility`
     - UML:Class, UML:Interface
     - name
   * - ''
     - :ref:`st_adapts`
     - UML:Dependency
     - order
   * - ''
     - :ref:`st_permits`
     - UML:Dependency
     - --
   * - ''
     - :ref:`st_for`
     - UML:Dependency
     - --
   * - ''
     - :ref:`st_subscribes`
     - UML:Dependency
     - --
   * - ''
     - :ref:`st_provides`
     - UML:InterfaceRealisation
     - --
   * - ''
     - :ref:`st_zcml`
     - UML:InterfaceRealization
     - --
   * - **plone**
     - .
     - .
     - .
   * - ''
     - :ref:`st_gsprofile`
     - UML:Package
     - None
   * - ''
     - :ref:`st_content_type`
     - UML:Class
     - create_content_class
   * - ''
     - :ref:`st_referencable`
     - UML:Class
     - None
   * - ''
     - :ref:`st_dynamic_view`
     - UML:Class
     - None
   * - ''
     - :ref:`st_view`
     - UML:Class, UML:Dependency
     - name. permission, layer
   * - **dexterity**
     - .
     - .
     - .
   * - ''
     - :ref:`st_python`
     - UML:Class
     - None
   * - ''
     - :ref:`st_xml`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_basic`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_categorization`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_publication`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_ownership`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_dublincore`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_namefromtitle`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_relateditems`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour_standard`
     - UML:Class
     - None
   * - ''
     - :ref:`st_behaviour`
     - UML:Class, UML:Dependency
     - **marker**
   * - (not implemented)
     - :ref:`st_Choice`
     - n/a
     - n/a
   * - (not implemented)
     - :ref:`st_RelationChoice`
     - n/a
     - n/a
   * - (not implemented)
     - :ref:`st_RelationList`
     - n/a
     - n/a
   * - .
     - :ref:`st_Tuple`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length, value_type
   * - .
     - :ref:`st_List`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length, value_type
   * - .
     - :ref:`st_Set`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length, value_type
   * - .
     - :ref:`st_Frozenset`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length, value_type
   * - .
     - :ref:`st_SourceText`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_Bytes`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_ASCII`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_DottedName`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_BytesLine`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_URI`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_ASCIILine`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_Id`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_Text`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_TextLine`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_Password`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length
   * - .
     - :ref:`st_Dict`
     - UML:Property
     - title, description, required, readonly, default, min_length, max_length, key_type, value_type
   * - .
     - :ref:`st_Bool`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_InterfaceField`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_NamedField`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_Relation`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_NamedImage`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_NamedBlobFile`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_NamedBlobImage`
     - UML:Property
     - title, description, required, readonly, default
   * - .
     - :ref:`st_RichText`
     - UML:Property
     - title, description, required, readonly, default, default_mime_type, output_mime_type, allowed_mime_types
   * - .
     - :ref:`st_Int`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Float`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Date`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Datetime`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Timedelta`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Decimal`
     - UML:Property
     - title, description, required, readonly, default, min, max
   * - .
     - :ref:`st_Object`
     - UML:Property
     - title, description, required, readonly, default, schema
   * - .
     - .
     - .
     - .
   * - **sqla**
     - .
     - .
     - .
   * - ''
     - :ref:`st_sqlcontent`
     - UML:Class
     - None
   * - .
     - :ref:`st_sql_table`
     - UML:Class
     - None
   * - .
     - :ref:`st_sql_concrete_table_inheritance`
     - UML:Class
     - None
   * - .
     - :ref:`st_joined_table_inheritance`
     - UML:Class
     - None
   * - .
     - :ref:`st_column`
     - UML:Property
     - index, not_null, unique, default, server_default
   * - .
     - :ref:`st_primary`
     - UML:Property
     - None
   * - .
     - :ref:`st_sql_type`
     - UML:PrimitiveType
     - None
   * - .
     - :ref:`st_z3c_saconfig`
     - UML:Package
     - engine_name, engine_url, session_name
   * - .
     - :ref:`st_attribute_mapped`
     - UML:Association
     - key
   * - .
     - :ref:`st_lazy`
     - UML:Association
     - laziness
   * - .
     - :ref:`st_ordered`
     - UML:Association
     - order_by

