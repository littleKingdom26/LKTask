#!/usr/bin/env python3
"""
선수 추가 스크립트
사용법: python3 add_player.py "이름" --number 번호 --position 포지션 [옵션들]
"""

import sys
import argparse
from player_model import Player, add_player

def main():
    parser = argparse.ArgumentParser(description='선수 정보 추가')
    parser.add_argument('name', help='선수 이름')
    parser.add_argument('--number', type=int, help='등번호')
    parser.add_argument('--position', choices=['FW', 'MF', 'DF', 'GK'], help='포지션 (FW, MF, DF, GK)')
    parser.add_argument('--goals', type=int, default=0, help='득점 수')
    parser.add_argument('--assists', type=int, default=0, help='도움 수')
    parser.add_argument('--matches', type=int, default=0, help='출전 경기 수')
    parser.add_argument('--minutes', type=int, default=0, help='출전 시간(분)')
    parser.add_argument('--yellow', type=int, default=0, help='노란 카드 수')
    parser.add_argument('--red', type=int, default=0, help='빨간 카드 수')
    
    args = parser.parse_args()
    
    # 선수 객체 생성
    player = Player(
        name=args.name,
        number=args.number,
        position=args.position,
        goals=args.goals,
        assists=args.assists,
        matches_played=args.matches,
        minutes_played=args.minutes,
        yellow_cards=args.yellow,
        red_cards=args.red
    )
    
    # 선수 추가
    added_player = add_player(player)
    
    print(f"\n✅ 선수가 추가되었습니다!")
    print(f"   이름: {added_player.name}")
    print(f"   번호: {added_player.number}")
    print(f"   포지션: {added_player.position}")
    print(f"   득점: {added_player.goals}")
    print(f"   도움: {added_player.assists}")
    print(f"   경기: {added_player.matches_played}")
    print(f"   출전: {added_player.minutes_played}분")
    print(f"   노란 카드: {added_player.yellow_cards}")
    print(f"   빨간 카드: {added_player.red_cards}")
    print(f"   ID: {added_player.id}")

if __name__ == '__main__':
    main()
