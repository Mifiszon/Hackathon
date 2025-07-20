import os
import zipfile
import pandas as pd
from datetime import datetime
from django.core.wsgi import get_wsgi_application
from urllib.parse import urlparse
import numpy as np
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = get_wsgi_application()

from kosciuszkon.serializers import (AgencySerializer, CalendarDatesSerializer, FeedInfoSerializer, RoutesSerializer,
                                     ShapesSerializer, TransfersSerializer, TripsSerializer, StopsSerializer, 
                                     CalendarSerializer, StopTimesSerializer)

def read_gtfs_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        gtfs_files = zip_ref.namelist()
        gtfs_data = {}
        for file in gtfs_files:
            if file.endswith('.txt'):
                with zip_ref.open(file) as f:
                    df = pd.read_csv(f)
                    table_name = os.path.splitext(file)[0]
                    gtfs_data[table_name] = df
    return gtfs_data

def convert_dates(df, date_columns):
    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], format='%Y%m%d', errors='coerce').dt.strftime('%Y-%m-%d')
    return df

def convert_url(df, url_columns):
    for column in url_columns:
        if column in df.columns:
            df[column] = df[column].apply(lambda x: x if pd.isna(x) or urlparse(str(x)).scheme in ['http', 'https'] else None)
    return df

def normalize_time(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
    except ValueError:
        # Handle times like '24:01:00'
        hours, minutes, seconds = map(int, time_str.split(':'))
        if hours >= 24:
            hours -= 24
            time_obj = (datetime(1, 1, 1, hours, minutes, seconds) + timedelta(days=1)).time()
        else:
            raise
    return time_obj

def clean_data(df):
    if 'location_type' in df.columns:
        df['location_type'] = df['location_type'].replace({np.nan: 0}).astype(int)
    if 'parent_station' in df.columns:
        df['parent_station'] = df['parent_station'].apply(lambda x: int(x) if pd.notnull(x) else None)
    if 'wheelchair_accessible' in df.columns:
        df['wheelchair_accessible'] = df['wheelchair_accessible'].replace({np.nan: 0}).astype(int)
    return df

def save_calendar(gtfs_data):
    print('calendar')
    if "calendar" in gtfs_data:
        df = gtfs_data['calendar']
        df = convert_dates(df, ['start_date', 'end_date'])
        for _, row in df.iterrows():
            serializer = CalendarSerializer(data=row.to_dict())
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in CalendarSerializer: {serializer.errors}")

def save_routes(gtfs_data):
    if 'routes' in gtfs_data:
        print('routes')
        df = convert_url(gtfs_data['routes'], ['route_url'])
        df['agency_id'] = df['agency_id'].replace({np.nan: None})
        
        for _, row in df.iterrows():
            row_data = row.to_dict()
            row_data['route_id'] = int(row_data['route_id'])
            serializer = RoutesSerializer(data=row_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in RoutesSerializer: {serializer.errors}")

def save_trips(gtfs_data):
    if 'trips' in gtfs_data:
        print('trips')
        df = gtfs_data['trips']
        df['direction_id'] = df['direction_id'].replace({np.nan: 0})
        df['wheelchair_accessible'] = df['wheelchair_accessible'].replace({np.nan: 0})
        for _, row in df.iterrows():
            data_row = row.to_dict()
            data_row['route'] = int(data_row['route_id'])
            data_row['direction_id'] = int(data_row['direction_id'])
            data_row['wheelchair_accessible'] = int(data_row['wheelchair_accessible'])
            data_row['service'] = int(data_row['service_id'])
            data_row['trip_id'] = int(data_row['trip_id'])

            serializer = TripsSerializer(data=data_row)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in TripsSerializer: {serializer.errors}")
                
def save_shapes(gtfs_data):
    if 'shapes' in gtfs_data:
        print('shapes')
        df = gtfs_data['shapes']
        for _, row in df.iterrows():
            serializer = ShapesSerializer(data=row.to_dict())
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in ShapesSerializer: {serializer.errors}")
                
def save_stops(gtfs_data):
    print('stops')
    if 'stops' in gtfs_data:
        df = gtfs_data['stops']
        df = convert_url(df, ['stop_url'])
        df = clean_data(df)
        for _, row in df.iterrows():
            print(row['stop_id'])
            row_data=row.to_dict()
            row_data['stop_id'] = int(row_data['stop_id'])
            
            serializer = StopsSerializer(data=row_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in StopsSerializer: {serializer.errors}")
                
def save_agency(gtfs_data):
    if 'agency' in gtfs_data:
        print('agency')
        df = gtfs_data['agency']
        for _, row in df.iterrows():
            serializer = AgencySerializer(data=row.to_dict())
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in AgencySerializer: {serializer.errors}")
                
def save_calendar_dates(gtfs_data):
    if 'calendar_dates' in gtfs_data:
        print('calendar_dates')
        df = gtfs_data['calendar_dates']
        df = convert_dates(df, ['date'])
        for _, row in df.iterrows():
            serializer = CalendarDatesSerializer(data=row.to_dict())
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in CalendarDatesSerializer: {serializer.errors}")
                
def save_feed_info(gtfs_data):
    if 'feed_info' in gtfs_data:
        print('feed_info')
        df = gtfs_data['feed_info']
        df = convert_dates(df, ['feed_start_date', 'feed_end_date'])
        for _, row in df.iterrows():
            serializer = FeedInfoSerializer(data=row.to_dict())
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in FeedInfoSerializer: {serializer.errors}")
def save_transfers(gtfs_data):
    if 'transfers' in gtfs_data:
        print('transfers')
        df = gtfs_data['transfers']
        for _, row in df.iterrows():
            row_data = row.to_dict()
            row_data['from_stop'] = int(row_data['from_stop_id'])
            row_data['to_stop'] = int(row_data['to_stop_id'])
            # print(row_data)
            serializer = TransfersSerializer(data=row_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in TransfersSerializer: {serializer.errors}")     
                
def save_stop_times(gtfs_data):
    if 'stop_times' in gtfs_data:
        print('stop_times')
        df = gtfs_data['stop_times']
        df['pickup_type'] = df['pickup_type'].replace({np.nan: 0}).astype(int)
        df['drop_off_type'] = df['drop_off_type'].replace({np.nan: 0}).astype(int)
        for _, row in df.iterrows():
            row_data = row.to_dict()
            row_data['pickup_type'] = int(row_data['pickup_type'])
            row_data['drop_off_type'] = int(row_data['drop_off_type'])
            
            row_data['arrival_time'] = normalize_time(row_data['arrival_time'])
            row_data['departure_time'] = normalize_time(row_data['departure_time'])
            row_data['trip'] = int(row_data['trip_id'])
            row_data['stop'] = int(row_data['stop_id'])
            
            serializer = StopTimesSerializer(data=row_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Error in StopTimesSerializer: {serializer.errors}")


if __name__ == "__main__":
    gtfs_zip_path = "resources/kau.zip"  # Change path to GTFS file
    gtfs_data = read_gtfs_zip(gtfs_zip_path)
    
    save_calendar(gtfs_data)
    save_shapes(gtfs_data)
    save_agency(gtfs_data)
    save_calendar_dates(gtfs_data)
    save_feed_info(gtfs_data)
    save_stops(gtfs_data)
    save_routes(gtfs_data)
    save_transfers(gtfs_data)
    save_trips(gtfs_data)
    save_stop_times(gtfs_data)
    
    print('Successfully loaded GTFS data')


# calendar shapes agency calendar_dates feed_info stops transfers routes trips stops_times