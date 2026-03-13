#!/usr/bin/env python3
"""
선수 목록 조회 스크립트
사용법: python3 list_players.py [--sort 기준]
"""

import argparse
from player_model import get_all_players

def main():
    parser = argparse.ArgumentParser(description='선수 목록 조회')
    parser.add_argument('--sort', choices=['number', 'name', 'goals', 'assists'], default='number', help='정렬 기준')
    parser.add_argument('--position', choices=['FW', 'MF', 'DF', 'GK'], help='포지션 필터')
    
    args = parser.parse_args()
    
    # 선수 목록 조회
    players = get_all_players()
    
    # 포지션 필터링
    if args.position:
        players = [p for p in players if p.position == args.position]
    
    # 정렬
    if args.sort == 'number':
        players.sort(key=lambda x: x.number or 999)
    elif args.sort == 'name':
        players.sort(key=lambda x: x.name)
    elif args.sort == 'goals':
        players.sort(key=lambda x: x.goals, reverse=True)
    elif args.sort == 'assists':
        players.sort(key=lambda x: x.assists, reverse=True)
    
    # 출력
    print(f"\n{'='*70}")
    print(f"📋 선수 목록 (총 {len(players)}명)")
    print(f"{'='*70}\n")
    
    if not players:
        print("등록된 선수가 없습니다.")
        return
    
    # 테이블 헤더
    header = f"{'번호':<6}{'이름':<15}{'포지션':<8}{'경기':<6}{'시간':<8}{'득점':<6}{'도움':<6}{'노란':<6}{'빨간':<6}"
    print(header)
    print("-" * 70)
    
    # 선수 정보 출력
    for player in players:
        row = f"{str(player.number):<6}{player.name:<15}{player.position:<8}{player.matches_played:<6}{player.minutes_played:<8}{player.goals:<6}{player.assists:<6}{player.yellow_cards:<6}{player.red_cards:<6}"
        print(row)
    
    print(f"\n{'='*70}")

if __name__ == '__main__':
    main()
