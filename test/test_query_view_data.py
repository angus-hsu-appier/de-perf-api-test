import os
import tableauserverclient as TSC

def test_query_view_All_Region_Realtime():
    SITE_ID = '25713daf-d1ec-4b89-87f4-aef3e2ca6dea'
    VIEW_ID = '9de5605e-5695-4497-b257-ea6880fc4cac'

    tableau_auth = TSC.TableauAuth(os.environ['TABLEAU_USERNAME'], os.environ['TABLEAU_PASSWORD'], '')
    server = TSC.Server('https://tableau-server-00.appier.info', use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        view = server.views.get_by_id(VIEW_ID)
        print("\nView name: {}".format(view.name))

        server.views.populate_csv(view)
        csv_data = b''.join(view.csv).decode('utf-8')
        #print(csv_data)
        assert csv_data is not None


def test_query_view_YDay_Dashboard():
    SITE_ID = '25713daf-d1ec-4b89-87f4-aef3e2ca6dea'
    VIEW_ID = 'd999453a-e25e-4672-868a-1b9000e38612'

    tableau_auth = TSC.TableauAuth(os.environ['TABLEAU_USERNAME'], os.environ['TABLEAU_PASSWORD'], '')
    server = TSC.Server('https://tableau-server-00.appier.info', use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        view = server.views.get_by_id(VIEW_ID)
        print("\nView name: {}".format(view.name))

        server.views.populate_csv(view)
        csv_data = b''.join(view.csv).decode('utf-8')
        #print(csv_data)
        assert csv_data is not None

