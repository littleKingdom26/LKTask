#!/usr/bin/env python3
"""
SQLite 데이터베이스 연결 및 초기화
"""

import sqlite3
import os
from datetime import datetime

# 데이터베이스 파일 경로
DB_PATH = '/home/littlekingdom/project/openclaw/suwonfc-stats/data/suwonfc.db'

def get_db_connection():
    """데이터베이스 연결"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # 딕셔너리처럼 접근 가능
    return conn

def init_database():
    """데이터베이스 초기화 (테이블 생성)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 선수 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number INTEGER,
            position TEXT,
            goals INTEGER DEFAULT 0,
            assists INTEGER DEFAULT 0,
            matches_played INTEGER DEFAULT 0,
            minutes_played INTEGER DEFAULT 0,
            yellow_cards INTEGER DEFAULT 0,
            red_cards INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 경기 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            opponent TEXT NOT NULL,
            home_away TEXT NOT NULL,
            date TEXT NOT NULL,
            score_for INTEGER,
            score_against INTEGER,
            result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 골 기록 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            match_id INTEGER,
            minute INTEGER,
            goal_type TEXT,
            FOREIGN KEY (player_id) REFERENCES players (id),
            FOREIGN KEY (match_id) REFERENCES matches (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    
    print("✅ 데이터베이스 초기화 완료!")
    print(f"   위치: {DB_PATH}")
    print("   테이블: players, matches, goals")

if __name__ == '__main__':
    # data 폴더 생성
    os.makedirs('/home/littlekingdom/project/openclaw/suwonfc-stats/data', exist_ok=True)
    
    # 데이터베이스 초기화
    init_database()
