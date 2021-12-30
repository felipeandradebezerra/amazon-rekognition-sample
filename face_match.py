#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import boto3
from urllib import urlopen

class FaceMatch:
    def __init__(self, source_url, target_url):
        """
        :param source: source image
        :param target: target image to run a similarity script
        """
        self.client = boto3.client('rekognition')
        self.source_url = source_url
        self.target_url = target_url

    def run(self):
        """Run the recognition algorithm"""
        try:
            source_bytes, target_bytes = self.download_images(self.source_url, self.target_url)
            faces = self.number_of_faces(target_bytes)

            if faces == 1:
                matches, similarity = self.compare_faces(source_bytes=source_bytes, target_bytes=target_bytes)
                if matches == 1:
                    return {"status": True, "similarity": similarity}
                else:
                    return {"status": False, "message": "Similarity not found"}
            else:
                return {"status": False, "message": "Sorry, multiple faces are not allowed"}
        except Exception as e:
            result = {"status": False, "message": "Sorry, we are unable to proceed with your request. Please check if the image link exists."}
            return result

    def download_images(self, source_url, target_url):
        """Download source and target images from a given link"""
        return (urlopen(source_url).read(), urlopen(target_url).read())

    def number_of_faces(self, target):
        """Check the number of faces in target image"""
        response = self.client.detect_faces(Image={'Bytes': target}, Attributes=['ALL'])
        return len(response['FaceDetails'])

    def compare_faces(self, source_bytes, target_bytes):
        """Compare faces"""
        similarity = None
        response = self.client.compare_faces(SimilarityThreshold=80,
                                      SourceImage={'Bytes': source_bytes},
                                      TargetImage={'Bytes': target_bytes})
        for faceMatch in response['FaceMatches']:
            similarity = str(faceMatch['Similarity'])
        return (len(response['FaceMatches']), similarity)

source = "https://site.com/_target.png"
target = "https://site.com/_source.png"

face = FaceMatch(source, target)
print(face.run())
