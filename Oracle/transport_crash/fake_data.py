#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/22 11:04 AM

__author__ = 'Miracle'

import random
import uuid
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import cx_Oracle
import faker

from core.fake_data import random_datetime

fake = faker.Faker()
G_OBJECTID = 200000000


def random_CRASH_DETAILS_TABLE():
    '''
    随机往CRASH_DETAILS_TABLE表里写数据
    D => CRASH_DETAILS_TABLE
    :param cur:
    :return:
    '''
    return dict(
        OBJECTID=G_OBJECTID,
        CRIMEID=random.randint(0, 30000000),
        CCN=random.randint(0, 100000000),
        PERSONID=random.randint(0, 90000000),
        PERSONTYPE=random.choice(('Bicyclist', 'Driver')),
        AGE=random.randint(18, 70),
        FATAL=random.choice(('Y', 'N')),
        MAJORINJURY=random.choice(('Y', 'N')),
        MINORINJURY=random.choice(('Y', 'N')),
        VEHICLEID=random.randint(0, 5000000),
        INVEHICLETYPE=random.choice((
            'Large/heavy Truck', 'Construction/industrial Equipment', 'Firearms', 'Bus', 'Passenger Van',
            'Atv (all Terrain Vehicle)', 'Motorhome/camper/rv (recreational Vehicle)', 'Trailer', 'Motor Cycle',
            'Cargo Van', 'Moped/scooter', 'Passenger Car/automobile', 'Pickup Truck', 'Watercraft/boat',
            'Suv (sport Utility Vehicle)', 'Farm Equipment', 'Aircraft', 'Drugs/ Narcotics', 'Other Vehicle',
            'Other Small/light Truck', 'Snow Mobile'
        )),
        TICKETISSUED=random.choice(('Y', 'N')),
        LICENSEPLATESTATE=random.choice((
            'Di', 'WV', 'OK', 'NJ', 'CA', 'Un', 'TN', 'KS', 'DE', 'FL', 'IN', 'AL', 'ND', 'Pu', 'MI', 'ME', 'DC', 'MT',
            'RI', 'IA', 'VT', 'CT', 'MO', 'ID', 'AZ', 'MN', 'AK', 'WY', 'VA', 'MA', 'WI', 'AR', 'NM', 'NE', 'IL', 'GA',
            'Vi', 'NH', 'CO', 'Am', 'LA', 'NV', 'MS', 'Ou', 'PA', 'NC', 'US', 'SD', 'MD', 'OH', 'Ot', 'UT', 'NY', 'SC',
            'TX', 'WA', 'HI', 'KY', 'OR'
        )),
        IMPAIRED=random.choice(('Y', 'N')),
        SPEEDING=random.choice(('Y', 'N')),
    )


def random_CRASHES_IN_DC():
    '''
    随机往CRASH_DETAILS_TABLE表里写数据
    C => CRASHES_IN_DC
    :param cur:
    :return:
    '''
    return dict(
        X=round(random.uniform(-180, 180), 7),
        Y=round(random.uniform(-180, 180), 7),
        OBJECTID=G_OBJECTID,
        CRIMEID=random.randint(0, 30000000),
        CCN=random.randint(0, 100000000),
        REPORTDATE=random_datetime(),
        ROUTEID=500000000,
        MEASURE=round(random.uniform(0, 10000), 1),
        OFFSET=round(random.uniform(0, 100), 4),
        STREETSEGID=random.randint(-10, 10000),
        ROADWAYSEGID=random.randint(0, 50000),
        FROMDATE=random_datetime(),
        TODATE=random_datetime(),
        MARID=random.randint(0, 1000000),
        ADDRESS=fake.address(),
        LATITUDE=float(fake.latitude()),
        LONGITUDE=float(fake.longitude()),
        XCOORD=round(random.uniform(0, 500000), 2),
        YCOORD=round(random.uniform(0, 500000), 2),
        WARD=random.choice(('Ward 8', 'Ward 6', 'Ward 2', 'Ward 4', 'Ward 1', 'Ward 5', '0', 'Ward 7', 'Ward 3')),
        EVENTID='{' + str(uuid.uuid4()) + '}',
        MAR_ADDRESS=fake.address(),
        MAR_SCORE=random.randint(0, 200),
        MAJORINJURIES_BICYCLIST=random.randint(0, 1),
        MINORINJURIES_BICYCLIST=random.randint(0, 2),
        UNKNOWNINJURIES_BICYCLIST=random.choice((1, 0, -999)),
        FATAL_BICYCLIST=random.randint(0, 2),
        MAJORINJURIES_DRIVER=random.randint(0, 7),
        MINORINJURIES_DRIVER=random.randint(0, 7),
        UNKNOWNINJURIES_DRIVER=random.randint(0, 5),
        FATAL_DRIVER=random.randint(0, 2),
        MAJORINJURIES_PEDESTRIAN=random.randint(0, 5),
        MINORINJURIES_PEDESTRIAN=random.randint(0, 4),
        UNKNOWNINJURIES_PEDESTRIAN=random.randint(0, 4),
        FATAL_PEDESTRIAN=random.randint(0, 2),
        TOTAL_VEHICLES=random.randint(0, 12),
        TOTAL_BICYCLES=random.randint(0, 2),
        TOTAL_PEDESTRIANS=random.randint(0, 12),
        PEDESTRIANSIMPAIRED=random.randint(0, 2),
        BICYCLISTSIMPAIRED=random.randint(0, 1),
        DRIVERSIMPAIRED=random.randint(0, 2),
        TOTAL_TAXIS=random.randint(0, 4),
        TOTAL_GOVERNMENT=random.randint(0, 4),
        SPEEDING_INVOLVED=random.randint(0, 6),
        NEARESTINTROUTEID=random.randint(10000000, 15000000),
        NEARESTINTSTREETNAME=fake.street_name(),
        OFFINTERSECTION=round(random.uniform(0, 50000), 6),
        INTAPPROACHDIRECTION=random.choice((
            'Southwest', 'North', 'Northeast', 'East', 'South', 'Northwest', 'Southeast', 'West'
        )),
        LOCATIONERROR='Crash point too far away from centerline',
        LASTUPDATEDATE=random_datetime(),
        MPDLATITUDE=float(fake.latitude()),
        MPDLONGITUDE=float(fake.longitude()),
        MPDGEOX=random.randint(390000, 410000),
        MPDGEOY=random.randint(120000, 150000),
    )


if __name__ == '__main__':


    interval = float(sys.argv[1])
    username = str(sys.argv[2])
    pwd = str(sys.argv[3])
    uri = str(sys.argv[4])

    with cx_Oracle.connect(username, pwd, uri) as conn:
        with conn.cursor() as cur:

            cur.execute('delete from "ARTHUR"."CRASH_DETAILS_TABLE" where OBJECTID >= 200000000')
            cur.execute('delete from "ARTHUR"."CRASHES_IN_DC" where OBJECTID >= 200000000')

            while True:
                G_OBJECTID += 1

                d_data = random_CRASH_DETAILS_TABLE()
                d_values = [':' + k for k, v in d_data.items()]
                d_sql = 'insert into ARTHUR."CRASH_DETAILS_TABLE" values(%s)' % (','.join(d_values))
                cur.execute(d_sql, dict(d_data))

                c_data = random_CRASHES_IN_DC()
                c_values = [':' + k for k, v in c_data.items()]
                c_sql = 'insert into ARTHUR."CRASHES_IN_DC" values(%s)' % (','.join(c_values))
                cur.execute(c_sql, dict(c_data))

                conn.commit()

                if (G_OBJECTID - 200000000) % 10 == 0:
                    print(f'随机产生{G_OBJECTID - 200000000}条数据')

                time.sleep(interval)
