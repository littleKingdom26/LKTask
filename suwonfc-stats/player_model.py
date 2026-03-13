#!/usr/bin/env python3
"""
선수 데이터 모델 및 CRUD 기능
"""

from datetime import datetime
from database import get_db_connection

class Player:
    """선수 클래스"""
    def __init__(self, name, number=None, position=None, goals=0, assists=0, 
                 matches_played=0, minutes_played=0, yellow_cards=0, red_cards=0, id=None):
        self.id = id
        self.name = name
        self.number = number
        self.position = position
        self.goals = goals
        self.assists = assists
        self.matches_played = matches_played
        self.minutes_played = minutes_played
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'position': self.position,
            'goals': self.goals,
            'assists': self.assists,
            'matches_played': self.matches_played,
            'minutes_played': self.minutes_played,
            'yellow_cards': self.yellow_cards,
            'red_cards': self.red_cards,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def __str__(self):
        """문자열 표현"""
        return f"{self.number}. {self.name} ({self.position}) - 득점: {self.goals}, 도움: {self.assists}"

def add_player(player):
    """선수 추가"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO players (name, number, position, goals, assists, matches_played, minutes_played, yellow_cards, red_cards)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        player.name, player.number, player.position, player.goals, player.assists,
        player.matches_played, player.minutes_played, player.yellow_cards, player.red_cards
    ))
    
    player.id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return player

def get_all_players():
    """모든 선수 목록 조회"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM players ORDER BY number')
    rows = cursor.fetchall()
    
    players = []
    for row in rows:
        player = Player(
            name=row['name'],
            number=row['number'],
            position=row['position'],
            goals=row['goals'],
            assists=row['assists'],
            matches_played=row['matches_played'],
            minutes_played=row['minutes_played'],
            yellow_cards=row['yellow_cards'],
            red_cards=row['red_cards'],
            id=row['id']
        )
        players.append(player)
    
    conn.close()
    return players

def get_player_by_id(player_id):
    """ID로 선수 조회"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM players WHERE id = ?', (player_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return Player(
            name=row['name'],
            number=row['number'],
            position=row['position'],
            goals=row['goals'],
            assists=row['assists'],
            matches_played=row['matches_played'],
            minutes_played=row['minutes_played'],
            yellow_cards=row['yellow_cards'],
            red_cards=row['red_cards'],
            id=row['id']
        )
    return None

def update_player(player):
    """선수 정보 수정"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    player.updated_at = datetime.now()
    
    cursor.execute('''
        UPDATE players 
        SET name=?, number=?, position=?, goals=?, assists=?, 
            matches_played=?, minutes_played=?, yellow_cards=?, red_cards=?, 
            updated_at=?
        WHERE id=?
    ''', (
        player.name, player.number, player.position, player.goals, player.assists,
        player.matches_played, player.minutes_played, player.yellow_cards, player.red_cards,
        player.updated_at, player.id
    ))
    
    conn.commit()
    conn.close()
    
    return player

def delete_player(player_id):
    """선수 삭제"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM players WHERE id = ?', (player_id,))
    conn.commit()
    conn.close()
    
    return True

if __name__ == '__main__':
    # 테스트: 선수 추가
    test_player = Player(
        name="하정우",
        number=11,
        position="FW",
        goals=2,
        assists=0,
        matches_played=2
    )
    
    added_player = add_player(test_player)
    print(f"✅ 선수 추가 완료: {added_player}")
    
    # 테스트: 전체 목록 조회
    print("\n📋 선수 목록:")
    players = get_all_players()
    for player in players:
        print(f"   {player}")
