# streamlit
import numpy as np
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit.components.v1 as components
import copy
# data reading
import pandas as pd

# helper functions
import helper_functions as friend
st.set_page_config(page_title="Data Analysis", page_icon="🛠", layout='wide')
hide_menu_style = """
        <style>
        # header {visibility: hidden;}
        # footer {visibility: hidden;}
        # MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# layout = None
# if 'stage' not in st.session_state:
#     layout = 'centered'
# else :
#     if st.session_state.stage !=4:
#         layout = 'wide'
#     else :
#         layout = 'centered'

# load data
def load_data():
    
    if 'load_data' in st.session_state:
        st.header(":green[Preview of upload data]")
        df = st.session_state.load_data['data']
        st.caption(f"shape of data, {df.shape}")
        st.dataframe(df)

        def moveon(direction):
            if direction=='reset':
                st.session_state.pop('load_data')
            else :
                assert direction=='next'
                st.session_state.stage +=1
                data_obj = friend.myData(st.session_state['load_data']['data'])
                st.session_state.load_data['data'] = data_obj

        left,middle,right = st.columns(3)
        middle.button("Reset",on_click=moveon,args=['reset'],key='reset_button')
        right.button("Next",on_click=moveon,args=['next'],key='next_button')
    
    else:
        st.header(":green[Upload your csv/excel]")
        filetype = st.radio("Choose type",options=['CSV','EXCEL'],horizontal=True)
        # uploading section

        if filetype =='CSV':
            uploaded_file = st.file_uploader("Upload",type=['csv'])
            if uploaded_file:
                # st.write(type(uploaded_file))
                try:
                    AADI_DATAFRAME = pd.read_csv(uploaded_file)
                    st.session_state['load_data'] = {'data':AADI_DATAFRAME}
                    st.checkbox("Done")
                except Exception as e:
                    st.error("Some error occurred")
        else:
            assert filetype=='EXCEL'
            uploaded_file = st.file_uploader("Upload",type=['xlsx','xlx'])
            
            if uploaded_file:
                # Read Excel file
                excel_data = pd.ExcelFile(uploaded_file)

                # Get sheet names
                sheet_names = excel_data.sheet_names
                left,right = st.columns(2)
                chosen_sheet = left.radio("Choose the sheet",
                                        options=sheet_names)
                def create_dataframe(excel,sheet):
                    AADI_DATAFRAME = pd.read_excel(excel,sheet_name=sheet)
                    st.session_state['load_data'] = {'data':AADI_DATAFRAME}
                    
                # right.markdown(":orange[Preview]")
                # right.dataframe(pd.read_excel(excel_data,chosen_sheet).head())
                right.button("Confirm Selection",on_click=create_dataframe,
                            args=[excel_data,chosen_sheet])

# identify target
def identify_target():
    if 'identify_target' not in st.session_state:
        # AADI_DATAFRAME = pd.read_csv("../product/data.csv")
        # AADI_DATAFRAME = pd.read_excel("./data.xlsx",sheet_name='Sheet1')
        
        previous_data = copy.deepcopy(st.session_state['load_data']['data'])
        st.session_state['identify_target'] = {'data':previous_data,
                                               'cache':{
                                                   'data':copy.deepcopy(previous_data),
                                                   'available_target_list':[]}
                                               }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = copy.deepcopy(st.session_state['identify_target']['cache'])

    current_data = st.session_state['cache']['data']

    st.markdown("### :green[Identify Target]")
    st.caption('dataframe preview')
    st.dataframe(current_data.dataframe.head())

    columns_selected = st.multiselect(
        "blank",
        options=current_data.dataframe.columns.tolist(),
        default=[current_data.dataframe.columns.tolist()[-1]],
        label_visibility="hidden",
        help="Choose the target(s)"
        )
    
    # prepare step summary
    
    #--------------------------------------
    def switch(direction,columns_selected):
            if direction=='next':
                st.session_state.stage +=1
                st.session_state['cache']['available_target_list'] = columns_selected
                
                st.session_state['identify_target']['data'].set_Xy(st.session_state['cache']['available_target_list'])
                st.session_state['identify_target']['cache'] = st.session_state['cache']
                st.session_state.pop('cache')
            
            elif direction=='pre':
                st.session_state.stage -=1
                st.session_state.pop('cache')
                st.session_state.pop('identify_target')
                st.session_state.pop('load_data')

    st.markdown('---')
    left,_,right = st.columns(3)
    right.button("Next Step",key='next',on_click=switch,args=['next',columns_selected])
    left.button("Previous",key='previous',on_click=switch,args=['pre'])

# Exclude columns
def exclude_columns():
    if 'exclude_columns' not in st.session_state:
        previous_data = copy.deepcopy(st.session_state['identify_target']['data'] )
        st.session_state['exclude_columns'] = {'data':previous_data,
                                               'cache':{'data':copy.deepcopy(previous_data),
                                                        'drop_column_list':[]
                                                        }
                                            }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = copy.deepcopy(st.session_state['exclude_columns']['cache'])
    
    current_data = st.session_state['cache']['data']

    st.markdown("### :green[exclude features]")
    st.caption('features preview')
    st.dataframe(current_data.X)

    excluded_features = st.multiselect(
        "haribol",
        options=current_data.available_feature_list,
        default=[],
        help="choose the variables which are not relevant :blue[if any]",
        key='excluded_features',
        label_visibility='hidden'
    )

    def switch(direction,columns_2_drop):
        if direction=='next':
            st.session_state.stage = st.session_state.stage + 1
            
            # create step summary
            data = st.session_state['cache']['data']
            data.drop_features(columns_2_drop)
            st.session_state['exclude_columns']  = {'data':copy.deepcopy(data),
                                                    'cache':{'data':copy.deepcopy(data),
                                                             'drop_column_list':columns_2_drop
                                                             }
                                                    }
            st.session_state.pop('cache')
        elif direction =='prev':
            st.session_state.stage = st.session_state.stage - 1
            st.session_state.pop('cache')
            st.session_state.pop('exclude_columns')
        else :
            st.session_state.pop("exclude_columns")
            st.session_state.pop('cache')

    st.markdown('---')
    left,middle,right = st.columns(3)
    left.button("Previous Step",key='prev',on_click=switch,args=['prev',excluded_features])
    middle.button("Reset",key='reset',on_click=switch,args=['reset',excluded_features])
    right.button("Next Step",key='next',on_click=switch,args=['next',excluded_features])

# Verify category of variables ~ numeric or categorical
def verify_column_category():
    if 'verify_column_category' not in st.session_state:
        previous_data = copy.deepcopy(st.session_state['exclude_columns']['data'])

        st.session_state['verify_column_category'] = {'data':previous_data,
                                                      'category_dict':previous_data.get_feature_cat_dict(),
                                                      'cache':{'data':copy.deepcopy(previous_data),
                                                               'category_dict':previous_data.get_feature_cat_dict()
                                                               }
                                                    }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = copy.deepcopy(st.session_state['verify_column_category']['cache'])


    st.markdown("### :green[Verify category of variables]")
    st.caption("click to toggle category")

    col_num,col_cat = st.columns([1,1])
    col_num.markdown("### :blue[numerical]")
    col_cat.markdown("### :violet[categorical]")

    def toggle(name):
        if st.session_state.cache['category_dict'][name] =='num':
            st.session_state.cache['category_dict'][name] = 'cat'
        else :
            st.session_state.cache['category_dict'][name] = 'num'

    category_dict = st.session_state.cache['category_dict']
    current_data = st.session_state.cache['data']
    for f in category_dict:
        if category_dict[f] == "num":
            col_num.button(f"{f} #{current_data.X[f].nunique()}",on_click=toggle,args=[f])
        else:
            col_cat.button(f"{f} #{current_data.X[f].nunique()}",on_click=toggle,args=[f])

    def switch(direction):
        if direction=='next':
            st.session_state.stage = st.session_state.stage + 1
            
            # create step summary
            st.session_state['verify_column_category']['category_dict'] = st.session_state['cache']['category_dict']
            st.session_state['verify_column_category']['cache'] = st.session_state.cache
            
            st.session_state.pop('cache')
        elif direction =='prev':
            st.session_state.stage = st.session_state.stage - 1
            st.session_state.pop('cache')
            st.session_state.pop('verify_column_category')
        else :
            st.session_state.pop('cache')
            st.session_state.pop('verify_column_category')

    st.markdown('---')
    left,middle,right = st.columns(3)
    left.button("Previous Step",key='prev',on_click=switch,args=['prev'])
    middle.button("Reset",key='reset',on_click=switch,args=['reset'])
    right.button("Next Step",key='next',on_click=switch,args=['next'])

# Data cleaning
def cleaning_data():
    if 'cleaning_data' not in st.session_state:
        previous_data = copy.deepcopy(st.session_state['verify_column_category']['data'])
        category_dict = st.session_state['verify_column_category']['category_dict']
        
        # update dtype as per category dict
        dtypedict = {}
        for column,dtype in category_dict.items():
            if dtype=='num':
                previous_data.dataframe[column] = pd.to_numeric(previous_data.dataframe[column],errors='ignore')

        st.session_state['cleaning_data'] = {
                                            'data':previous_data,
                                            'category_dict':category_dict,
                                            'cache':{'data': copy.deepcopy(previous_data),
                                                    'category_dict': category_dict,
                                                    'filters': {},
                                                    'na_step_done':False,
                                                    'non_numeric_step_done':False,
                                                    'categorical_merging':False
                                                    }
                                            }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = copy.deepcopy(st.session_state['cleaning_data']['cache'])


    current_data_pre_filter = copy.deepcopy(st.session_state.cleaning_data['data'])
    category_dict = st.session_state.cache['category_dict']
    
    # some filter for previewing na things
    name,buttons = st.columns([3,1])
    filter_select_option = set(current_data_pre_filter.available_feature_list) - set(st.session_state.cache['filters'].keys())
    filter_variable_name = name.selectbox("Choose",label_visibility='hidden',
                                          options=filter_select_option)
    buttons.markdown("")
    buttons.markdown("")

    # some filter handlers
    ## remove from filter
    def remove_from_filter(column_name):
        st.session_state.cache['filters'].pop(column_name)
    
    ## add to the filter
    def add_name_to_filter(column):
        column_filter_info = {'is_numerical':None,
                              'lower_bound':-1,
                              'upper_bound':-1,
                              'allowed_values':[],
                              'describe':None
                              }
        if category_dict[column] =='num':
            column_filter_info['is_numerical'] = True
            use_only_numerical_value = pd.to_numeric(current_data_pre_filter.X[column],errors='coerce')

            column_filter_info['lower_bound'] = use_only_numerical_value.min()
            column_filter_info['upper_bound'] = use_only_numerical_value.max()
            column_filter_info['describe'] = use_only_numerical_value.describe(percentiles=[i/10 for i in range(1,11)]).to_frame().rename(columns={column:''}).T
        
        else :

            column_filter_info['is_numerical'] = False
            column_filter_info['allowed_values'] = current_data_pre_filter.X.dropna(subset=[column])[column].unique().tolist()
            count_info = current_data_pre_filter.X[column].value_counts().to_frame().rename(columns={column:'#'})
            count_info['%'] = count_info['#']/count_info['#'].sum()
            
            count_info['%'] = count_info['%'].map('{:.1%}'.format)
            count_info['#'] = count_info['#'].map('{:,.0f}'.format)
            column_filter_info['describe'] = count_info.T
        
        st.session_state.cache['filters'][column] = column_filter_info
    
    buttons.button('Add ➕',on_click=add_name_to_filter,args=[filter_variable_name])
    st.markdown('---')
    
    pandas_query = {}
    # {var:[lower,upper]}
    # {var:[allowed]}
    
    # displaying filters
    for column_name,filterinfo in st.session_state.cache["filters"].items():
        # categorical filters
        if category_dict[column_name] =='cat':

            name,multi_select_box,col3 = st.columns([2,3,1])            
            name.markdown("")
            col3.markdown("")
            name.markdown("")
            col3.markdown("")

            name.markdown(column_name)
            if name.checkbox('show details',key='info'+column_name):
                st.dataframe(filterinfo['describe'])
            selected_choices = multi_select_box.multiselect('hide',label_visibility='hidden',
                                         options=filterinfo['allowed_values'],
                                         default=filterinfo['allowed_values'],
                                         key=column_name+'_choicebox')
            col3.button("❌remove",on_click=remove_from_filter,args=[column_name],key=column_name)
            
            pandas_query[column_name] = selected_choices
        
        
        
        
        # numerical filters
        else :
            name,lower,upper,col4 = st.columns([1.2,1,1,1])
            name.markdown("")
            name.markdown("")
            col4.markdown("")
            col4.markdown("")

            name.markdown(column_name)
            if name.checkbox('show details',key='info'+column_name):
                st.dataframe(filterinfo['describe'])
            selected_min_value = lower.number_input("min",
                                        min_value=filterinfo['lower_bound'],
                                        max_value=filterinfo['upper_bound'],
                                        value=filterinfo['lower_bound'],
                                        key=column_name + '_min_input')
            
            selected_max_value = upper.number_input("min",
                                        min_value=filterinfo['lower_bound'],
                                        max_value=filterinfo['upper_bound'],
                                        value=filterinfo['upper_bound'],
                                        key=column_name + '_max_input')
            col4.button("❌remove",on_click=remove_from_filter,args=[column_name],key=column_name)
            pandas_query[column_name] = [selected_min_value,selected_max_value]
        st.markdown('---')    

    # build the query
    query_list = []
    for column_name,query in pandas_query.items():
        if category_dict[column_name] =='num':
            m,M = query
            query_list.append(f"`{column_name}` >= {m} & `{column_name}` <= {M}")
        else :
            query_list.append(f"`{column_name}` in {query}")
    
    # st.write(query_list)
    final_query = ' & '.join(query_list)

    # apply the query if asked to apply
    def apply_the_query(query):
        st.session_state.cache['data'] = copy.deepcopy(st.session_state.cleaning_data['data'])
        st.session_state.cache['data'].apply_query(query)
        st.session_state.cache['na_step_done'] = False
        st.session_state.cache['categorical_merging'] = False
        st.session_state.cache['non_numeric_step_done'] = False
    st.button("Apply the filters",on_click=apply_the_query,args=[final_query],key='apply_query_button')

    filtered_data = st.session_state.cache['data']
    st.write(f"Shape after putting filters : {filtered_data.dataframe.shape}")
    # =====================dealing with na values
    st.markdown("## :green[Dealing with `na` values]")

    if st.session_state.cache['na_step_done']:
        st.success("no more na values in the dataframe")
    
    else:
        # create dataframe for na values for all columns
        na_info = filtered_data.X.isna().sum().to_frame().reset_index()
        na_info.columns=['column','na_count']
        na_info = na_info.query('na_count >0')
        na_info['%'] = na_info.na_count/len(filtered_data.dataframe)
        na_info['%'] = na_info['%'].map('{:.1%}'.format)

        na_info['type'] = na_info.column.apply(lambda x : category_dict[x])


        if len(na_info) ==0:
            st.session_state.cache['na_step_done'] = True
            st.success("no more na values in the dataframe")
        else:
            # Action on na values
            # Drop or replace
            left,right = st.columns([3,2])
            left.caption(f"Total rows: {len(filtered_data.dataframe):,.0f}")

            ## display the na-summary data frame
            grid_builder = GridOptionsBuilder.from_dataframe(na_info)
            grid_builder.configure_columns(list(na_info.columns), editable=True)
            grid_builder.configure_selection('multiple', use_checkbox=True,
                                             header_checkbox=True)
            grid_options = grid_builder.build()
            left.markdown(":orange[Select the columns to apply]")
            with left:
                grid_result = AgGrid(na_info,gridOptions=grid_options)
            # right.write(grid_result['selected_rows'])
            action_columns = [j['column'] for j in grid_result['selected_rows']]
            # right.write(action_columns)

            action_decision = right.radio(":orange[What would you like to do?]",
                                        options=['Replace-Mean','Drop','Replace-Custom'],
                                        )
            
            # select_all = right.checkbox("Select All",key='select_all',value=True)
            # for column_name in na_info.index.tolist():
            #     if right.checkbox(column_name,key=column_name,value=select_all):
            #         action_columns.append(column_name)
            
            ## ----------Replace for given set of columns and given values for na
            if action_decision =='Replace-Custom':
                replacevalue = right.text_input(":orange[enter the value to replace with]")
                replacevalue = replacevalue.strip()
                
                def apply(column_list,replacevalue):
                    st.session_state['cache']['data'].fillna(column_list,replacevalue)
                if action_columns and replacevalue:
                    right.button('Replace the Values',on_click=apply,args=[action_columns,replacevalue])



            elif action_decision=='Replace-Mean':
                def apply(column_list):
                    column_list = list(set(column_list) - set([col for col,coltype in category_dict.items() if coltype=='cat']))
                    st.session_state['cache']['data'].fillna_by_mean(column_list)
                if action_columns:
                    right.button("Replace with Means",on_click=apply,args=[action_columns])
            
            
            else:
            ## ---------- drop the na values for subset of columns
                assert action_decision =='Drop'
                def apply(column_list):
                    st.session_state['cache']['data'].dropna(column_list)
                if action_columns:
                    right.button('Drop Selected columns',on_click=apply,args=[action_columns])
                    drop_rows = na_info.query(f"column in {action_columns} ").na_count.sum()
                    right.caption(f'This will drop {drop_rows} rows | total {len(filtered_data.dataframe)}')
                    right.caption(f"drop {drop_rows/len(filtered_data.dataframe):.1%} of data")
    
    if not st.session_state.cache['na_step_done']:
        return
    

    # dealing with non-numeric values
    # only for numeric cases
    st.markdown('## :green[Dealing with non-numeric values]')
    
    if st.session_state.cache['non_numeric_step_done']:
        st.success("all numerical columns are fine now")
    else :

        # find the numeric columns with non-numeric data
        problematic_column_dict = {}
        for column_name in filtered_data.get_features():
            if category_dict[column_name]=='num':
                numerical_series = pd.to_numeric(filtered_data.X[column_name],errors='coerce')
                if numerical_series.isna().sum() >0:
                    problematic_column_dict[column_name] = filtered_data.X[column_name][numerical_series.isna()].value_counts().to_frame()
        
        if not bool(problematic_column_dict):
            st.session_state.cache['non_numeric_step_done'] = True
            st.success("all numerical columns are fine now")
        else :
            # Actual dealing with the problamatic columns
            action_column =  st.radio("These columns have some difficulty",
                                      options=problematic_column_dict.keys(),
                                      horizontal=True)
            left,middle,right = st.columns([2,3,2])
            
            left.dataframe(problematic_column_dict[action_column])
            action_decision  = middle.radio("What to do 💁‍♂️",options=['Drop',"Replace"],
                                            horizontal=True)
            
            special_values = problematic_column_dict[action_column].index.tolist()
            
            action_values = []
            select_all=middle.checkbox("Select All",key='select-all',value=True)
            for value in special_values[:50]:
                if middle.checkbox(value,value=select_all,key=value):
                    action_values.append(value)
            if len(special_values)>50:
                middle.warning(f"AND some more {len(special_values)-50}  values")   
            
            ### Action ---Drop
            if action_decision=='Drop':
                if action_values:
                    def apply(column_name,value_list):
                        st.session_state.cache['data'].drop_by_value(column_name,value_list)

                    right.button('Apply',on_click=apply,args=[action_column,action_values])
            
            
            else :
            ### Action ---- Replace
                assert action_decision=='Replace'
                replace_value = right.text_input("Value to Replace with")
                if action_values and replace_value:
                    def apply(column_name,value_list,replace_value):
                        replace_list = [replace_value for i in value_list]
                        replace_dict = dict(zip(value_list,replace_list))
                        st.session_state.cache['data'].replace_values(column_name,replace_dict)

                    right.button("Apply",on_click=apply,args=[action_column,action_values,replace_value])
    

    if not st.session_state.cache['non_numeric_step_done']:
        return
    
    ## Dealing with categorical values
    st.markdown("## :green[Treating Categorical values]")
    categorical_column_list = [i for i in filtered_data.X.columns.tolist() \
                               if category_dict[i]=='cat']
    left,right = st.columns([1,1])
    with left:
        category_summary_df = filtered_data.X[categorical_column_list].nunique().to_frame().reset_index()
        category_summary_df.columns = ['Column','#unique']
        ## display the na-summary data frame
        grid_builder = GridOptionsBuilder.from_dataframe(category_summary_df)
        grid_builder.configure_selection('single', use_checkbox=True)
        grid_options = grid_builder.build()
        grid_response = AgGrid(category_summary_df,gridOptions=grid_options)
    
    action_column = grid_response['selected_rows'][0]['Column'] if grid_response['selected_rows'] else None
    
    if action_column:
        selected_column_info = filtered_data.X[action_column] \
                     .value_counts().to_frame().reset_index()\
                     .rename(columns={action_column:"#",'index':f"{action_column}-values"})
        selected_column_info['%'] = selected_column_info['#']/selected_column_info['#'].sum()
        selected_column_info['%'] = selected_column_info['%'].map('{:.1%}'.format)
        selected_column_info['#'] = selected_column_info['#'].map('{:,.0f}'.format)

        ## display the na-summary data frame
        grid_builder = GridOptionsBuilder.from_dataframe(selected_column_info)
        grid_builder.configure_selection('multiple', use_checkbox=True,header_checkbox=True)
        grid_options = grid_builder.build()
        right.markdown(":orange[Select Values to merge]")
        with right:
            grid_response = AgGrid(selected_column_info,gridOptions=grid_options)
        action_values = [i[f"{action_column}-values"] for i in grid_response['selected_rows']]
        right.markdown(":violet[Choose the final value]")  

        if len(action_values)>1:
                
            final_value = right.radio('hide',options=[*action_values,'others','my choice'],
                                        label_visibility='hidden')
            # handler function
            def merge(column_name,value_list,final_value):
                st.session_state.cache['data'].merge_categorical(column_name,value_list,final_value)                

            if final_value =='my choice':
                final_value_other = right.text_input("Enter your choice")
                final_value_other = final_value_other.strip()

            if final_value !='my choice':
                right.button("Apply",on_click=merge,args=[action_column,action_values,final_value])
            else:
                ## user must enter another value
                if final_value_other:
                    right.button("Apply",on_click=merge,args=[action_column,action_values,final_value_other])
    else:
        right.markdown(":orange[Check in the table to merge]")


    ## next previous
    def switch(direction):
        if direction=='next':
            st.session_state.stage += 1
            
            # Step summary
            st.session_state['cleaning_data']['data'] = copy.deepcopy(st.session_state.cache['data'])
            st.session_state['cleaning_data']['cache'] = st.session_state.cache
            st.session_state.pop('cache')

        elif direction == 'prev':
            st.session_state.stage -= 1
            st.session_state.pop('cache')
            st.session_state.pop('cleaning_data')
        else :
            assert direction=='reset'
            st.session_state.pop('cache')
            st.session_state.pop('cleaning_data')
    
    st.markdown('---')
    left,middle,right = st.columns(3)
    left.button("Previous Step",key='prev',on_click=switch,args=['prev'])
    middle.button("Reset",key='reset',on_click=switch,args=['reset'])
    right.button("Next Step",key='next',on_click=switch,args=['next']) 


# slice the data
def apply_filters():    
    if 'apply_filters' not in st.session_state:
        previous_data = copy.deepcopy(st.session_state['cleaning_data']['data'])
        category_dict = st.session_state['cleaning_data']['category_dict']
        dtypedict = {}
        for column,dtype in category_dict.items():
            dtypedict[column] = float if dtype =='num' else object
        
        previous_data.set_dtype(dtypedict)
        st.session_state['apply_filters'] = {'data':previous_data,
                                             'category_dict':category_dict,
                                            'cache':{'data':copy.deepcopy(previous_data),
                                                     'category_dict':category_dict,
                                                     'filters':{}
                                                     }
                                            }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = st.session_state.apply_filters['cache']
        #                              {'data:data_object,
        #                                'category_dict': 
        #                                'filters':{'var':{"isnum":True,
        #                                                'lower_bound':
        #                                                'upper_bound':,
        #                                                'allowed_value':,
        #                                                 'describe':dataframe
        #                                                }
        #                                         }
        #                              }
    # st.dataframe(st.session_state['cache']['data'].dataframe.dtypes.to_frame())
    st.markdown("### :green[Slicing the Data]")

    current_data = st.session_state.cache['data']
    category_dict = st.session_state.cache['category_dict']

    # create column addition field
    name,button = st.columns([3,1])
    select_options = set(current_data.available_feature_list)-set(st.session_state.cache['filters'].keys())
    variable_name = name.selectbox("Choose",label_visibility='hidden',
                                   options=select_options)
    button.markdown("")
    button.markdown("")

    ## some filter handlers
    ## remove from filter
    def remove_from_filter(column_name):
        st.session_state.cache['filters'].pop(column_name)
    ## add to the filter
    def add_name_to_filter(column):
        column_filter_info = {'is_numerical':None,
                              'lower_bound':-1,
                              'upper_bound':-1,
                              'allowed_values':[],
                              'describe':None
                              }
        if category_dict[column] =='num':
            column_filter_info['is_numerical'] = True
            column_filter_info['lower_bound'] = current_data.X[column].min()
            column_filter_info['upper_bound'] = current_data.X[column].max()
            column_filter_info['describe'] = current_data.X[column].describe(percentiles=[i/10 for i in range(1,11)]).to_frame().rename(columns={column:''}).T
        else :
            column_filter_info['is_numerical'] = False
            column_filter_info['allowed_values'] = current_data.X[column].unique().tolist()
            count_info = current_data.X[column].value_counts().to_frame().rename(columns={column:'#'})
            count_info['%'] = count_info['#']/count_info['#'].sum()
            
            count_info['%'] = count_info['%'].map('{:.1%}'.format)
            count_info['#'] = count_info['#'].map('{:,.0f}'.format)
            column_filter_info['describe'] = count_info.T
        
        st.session_state.cache['filters'][column] = column_filter_info

    button.button('Add ➕',on_click=add_name_to_filter,args=[variable_name])
    st.markdown('---')



    pandas_query = {}
    # {var:[lower,upper]}
    # {var:[allowed]}
    for column_name,filterinfo in st.session_state.cache["filters"].items():
        # categorical filters
        if category_dict[column_name] =='cat':

            name,multi_select_box,col3 = st.columns([2,3,1])            
            name.markdown("")
            col3.markdown("")
            name.markdown("")
            col3.markdown("")

            name.markdown(column_name)
            if name.checkbox('show details',key='info'+column_name):
                st.dataframe(filterinfo['describe'])
            selected_choices = multi_select_box.multiselect('hide',label_visibility='hidden',
                                         options=filterinfo['allowed_values'],
                                         default=filterinfo['allowed_values'],
                                         key=column_name+'_choicebox')
            col3.button("❌remove",on_click=remove_from_filter,args=[column_name],key=column_name)
            
            pandas_query[column_name] = selected_choices
        # numerical filters
        else :
            name,lower,upper,col4 = st.columns([1.2,1,1,1])
            name.markdown("")
            name.markdown("")
            col4.markdown("")
            col4.markdown("")

            name.markdown(column_name)
            if name.checkbox('show details',key='info'+column_name):
                st.dataframe(filterinfo['describe'])
            selected_min_value = lower.number_input("min",
                                        min_value=filterinfo['lower_bound'],
                                        max_value=filterinfo['upper_bound'],
                                        value=filterinfo['lower_bound'],
                                        key=column_name + '_min_input')
            
            selected_max_value = upper.number_input("min",
                                        min_value=filterinfo['lower_bound'],
                                        max_value=filterinfo['upper_bound'],
                                        value=filterinfo['upper_bound'],
                                        key=column_name + '_max_input')
            col4.button("❌remove",on_click=remove_from_filter,args=[column_name],key=column_name)
            pandas_query[column_name] = [selected_min_value,selected_max_value]
        st.markdown('---')
    
    # st.write(st.session_state.cache.get("filters",{}))
    # st.write(pandas_query)
    
    # build the query
    query_list = []
    for column_name,query in pandas_query.items():
        if category_dict[column_name] =='num':
            m,M = query
            query_list.append(f"`{column_name}` >= {m} & `{column_name}` <= {M}")
        else :
            query_list.append(f"`{column_name}` in {query}")
    
    # st.write(query_list)
    final_query = ' & '.join(query_list)
    queried_df = current_data.dataframe.query(final_query) if query_list else current_data.dataframe.copy()

    left,right = st.columns(2)
    left.markdown(f":green[Original Dataframe {'-'*5}#:violet[{len(current_data.dataframe)}]]")
    right.markdown(f":green[Filtered Dataframe {'-'*5}#:violet[{len(queried_df)}]]")
    # left.dataframe(current_data.dataframe)
    # right.dataframe(queried_df)

    # 
    st.markdown("### :green[Data Clipping]")
    numerical_columns = [colname for colname,coltype in category_dict.items() if coltype =='num']
    univariatedf=queried_df[numerical_columns].describe(percentiles=[.05,.99,*[i/10 for i in range(11)]]).T.drop(columns=['count','max','mean','std','min'])
    univariatedf['min_clip'] = .05
    univariatedf['max_clip'] = .995
    st.dataframe(univariatedf)
    def copy_to_clipboard(dataframe):
        dataframe.to_clipboard()
    st.button("Copy Univariate",on_click=copy_to_clipboard,args=[univariatedf])

    clipping_dict = {}
    for column_name in univariatedf.index:
        clipping_dict[column_name] = [univariatedf.loc[column_name,'min_clip'],
                                      univariatedf.loc[column_name,'max_clip']]
    ## page navigation
    def switch(direction,final_query,cliping_dict):
        if direction=='next':
            st.session_state.stage +=1
            
            # create summary
            st.session_state.cache['data'].apply_query(final_query)
            st.session_state.cache['data'].clip_my_data(clipping_dict)

            st.session_state['apply_filters']['data'] =copy.deepcopy(st.session_state.cache['data'])
            st.session_state['apply_filters']['cache'] = st.session_state.cache

            st.session_state.pop('cache')
        elif direction == 'prev':
            st.session_state.stage -= 1
            st.session_state.pop('cache')
            st.session_state.pop('apply_filters')
        else :
            assert direction=='reset'
            st.session_state.pop('cache')
            st.session_state.pop('apply_filters')
    st.markdown('---')
    left,middle,right = st.columns(3)
    left.button("Previous Step",key='prev',on_click=switch,args=['prev',final_query,-2])
    middle.button("Reset",key='reset',on_click=switch,args=['reset',final_query,-1])
    right.button("Next Step",key='next',on_click=switch,args=['next',final_query,clipping_dict])            


# Choose features and result
def choose_n_result():

    if 'choose_n_result' not in st.session_state:
        previous_data = copy.deepcopy(st.session_state['apply_filters']['data'])
        category_dict = st.session_state['apply_filters']['category_dict']
        st.session_state['choose_n_result'] = {'data':previous_data,
                                               'category_dict':category_dict,
                                               'cache':
                                                        {'data':copy.deepcopy(previous_data),
                                                         'category_dict':category_dict,
                                                         'run_the_model':False}
                                                }
    if 'cache' not in st.session_state:
        st.session_state['cache'] = copy.deepcopy(st.session_state['choose_n_result']['cache'])
    #--------
    current_data = st.session_state.cache['data']
    category_dict = st.session_state.cache['category_dict']
    # st.warning(st.session_state['cache']['data'].dataframe.shape)
    # st.write(st.session_state)
    st.markdown("# :green[Select the variables and :red[target]]")

    left,middle,right,col4 = st.columns(4)
    default_choice = left.checkbox("Select All",key='default_selection',value=True)
    selected_features = []

    for index,column_name in enumerate(sorted(current_data.available_feature_list)):
        modulo3 = index%3
        if modulo3 ==0:
            if middle.checkbox(column_name.replace("_"," ").title(),
                               value=default_choice,
                               key=column_name+"_choosen"):
                selected_features.append(column_name)
        elif modulo3 ==1:
            if right.checkbox(column_name.replace("_"," ").title(),
                               value=default_choice,
                               key=column_name+"_choosen"):
                selected_features.append(column_name)
        elif modulo3 ==2:
            if left.checkbox(column_name.replace("_"," ").title(),
                               value=default_choice,
                               key=column_name+"_choosen"):
                selected_features.append(column_name)
    
    selected_target = col4.radio(":red[Choose the target]",options=current_data.available_target_list
                                )
    col4.caption(f"good: {len(current_data.dataframe[selected_target])}, bad: {current_data.dataframe[selected_target].sum()}")
    # warning for not selecting anything
    if not selected_features:
        st.error('Select at least one feature')
        return
    st.markdown('---')

    # display some information about data
    left,right = st.columns([1,4])
    right.caption(f"number of rows of data, {current_data.dataframe.shape}")
    
    if left.checkbox("Show univariates",key="display_univariate_button"):

        numerical_columns = [column_name for column_name in selected_features if category_dict[column_name]=='num']
        univariate_to_show = st.session_state.cache['data'].dataframe[numerical_columns].describe(percentiles=[.05,.99,*[i/10 for i in range(11)]]).T.drop(columns=['count','max','mean','std','min'])
        st.dataframe(univariate_to_show)
    st.markdown('---')
    



    def rerun_handler():
        st.session_state['cache']['run_the_model'] = True

    st.button("Rerun" if current_data.have_html else "Run",on_click=rerun_handler)
    # Create the Tree
    if st.session_state.cache['run_the_model']:
        current_data.run_the_model(selected_features,selected_target,st.session_state['cache']['category_dict'])
        st.session_state.cache['run_the_model'] = False
        st.success("Successfully run the model")
        st.write(":green[created the file 'analysis.html']")
    
    if current_data.have_html:
        # st.markdown(,unsafe_allow_html=True)
        components.html(current_data.dtree_html_content,height=500)
        st.download_button("Download tree",mime='text/html',key='downloadtree',
                           data=current_data.dtree_html_content,file_name='analysis.html')

    # st.write(category_dict)
    def switch(stage_index):
        st.session_state.pop("cache")
        if stage_index==0:
            st.session_state.pop('load_data')
            st.session_state.pop('identify_target')
            st.session_state.pop('exclude_columns')
            st.session_state.pop('verify_column_category')
            st.session_state.pop('cleaning_data')
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')

        elif stage_index==1:
            st.session_state.pop('identify_target')
            st.session_state.pop('exclude_columns')
            st.session_state.pop('verify_column_category')
            st.session_state.pop('cleaning_data')
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')

        elif stage_index ==2:
            st.session_state.pop('exclude_columns')
            st.session_state.pop('verify_column_category')
            st.session_state.pop('cleaning_data')
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')

        elif stage_index==3:
            st.session_state.pop('verify_column_category')
            st.session_state.pop('cleaning_data')
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')

        elif stage_index ==4:
            st.session_state.pop('cleaning_data')
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')
        
        elif stage_index ==5:
            st.session_state.pop('apply_filters')
            st.session_state.pop('choose_n_result')

        st.session_state.stage = stage_index

    pagelinks = {'load_data':0,
                "identify_target":1,
                "exclude_columns":2,
                "verify_column_category":3,
                "cleaning_data":4,
                "apply_filters":5}
    st.markdown('---')
    for pagename,stage in pagelinks.items():
        st.button(pagename.replace("-"," ").title(),key='goto'+pagename,on_click=switch,
                  args=[stage])


pagemap = {0: load_data,
           1:identify_target,
           2:exclude_columns,
           3:verify_column_category,
           4:cleaning_data,
           5:apply_filters,
           6:choose_n_result}
# states = [
# 'cache',
# "identify_target",
# "exclude_columns",
# "verify_column_category",
# "cleaning_data",
# "apply_filters"]
# choice=st.radio("stage",[0,1,2,3,4,5],horizontal=True)

# if states[choice] in st.session_state:
#     st.write(st.session_state[states[choice]])



# to freeze at sometime
# st.session_state['cache']['data'].dataframe.to_csv('statue.csv',index=False)
if 'stage' not in st.session_state.keys():
    st.session_state.stage = 0
    pagemap[st.session_state.stage]()

elif st.session_state.stage in pagemap.keys() :
    pagemap[st.session_state.stage]()
else :
    st.error('something went wrong')

    def reset():
        st.session_state.stage = 1
    st.button('Re-Start',on_click=reset)
