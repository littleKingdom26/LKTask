#!/usr/bin/env python3
"""
선수 정보 수정 스크립트
사용법: python3 update_player.py [선수 ID] --goals 득점 [옵션들]
"""

import sys
import argparse
from player_model import get_player_by_id, update_player

def main():
    parser = argparse.ArgumentParser(description='선수 정보 수정')
    parser.add_argument('player_id', type=int, help='선수 ID')
    parser.add_argument('--goals', type=int, help='득점 수')
    parser.add_argument('--assists', type=int, help='도움 수')
    parser.add_argument('--matches', type=int, help='출전 경기 수')
    parser.add_argument('--minutes', type=int, help='출전 시간(분)')
    parser.add_argument('--yellow', type=int, help='노란 카드 수')
    parser.add_argument('--red', type=int, help='빨간 카드 수')
    
    args = parser.parse_args()
    
    # 선수 조회
    player = get_player_by_id(args.player_id)
    if not player:
        print(f"⚠️ ID가 {args.player_id}인 선수를 찾을 수 없습니다.")
        return
    
    # 수정 전 정보 출력
    print(f"\n📋 수정 전: {player}")
    
    # 업데이트할 값들만 적용
    if args.goals is not None:
        player.goals = args.goals
    if args.assists is not None:
        player.assists = args.assists
    if args.matches is not None:
        player.matches_played = args.matches
    if args.minutes is not None:
        player.minutes_played = args.minutes
    if args.yellow is not None:
        player.yellow_cards = args.yellow
    if args.red is not None:
        player.red_cards = args.red
    
    # 수정
    updated_player = update_player(player)
    
    print(f"\n✅ 선수 정보가 수정되었습니다!")
    print(f"   ID: {updated_player.id}")
    print(f"   이름: {updated_player.name}")
    print(f"   득점: {updated_player.goals}")
    print(f"   도움: {updated_player.assists}")
    print(f"   경기: {updated_player.matches_played}")
    print(f"   출전: {updated_player.minutes_played}분")

if __name__ == '__main__':
    main()
