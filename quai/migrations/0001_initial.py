# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('quai_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_called', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('in_recontacting_loop', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('quai', ['Contact'])

        # Adding model 'Meet'
        db.create_table('quai_meet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quai.Contact'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('quai', ['Meet'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('quai_contact')

        # Deleting model 'Meet'
        db.delete_table('quai_meet')


    models = {
        'quai.contact': {
            'Meta': {'object_name': 'Contact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_recontacting_loop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_called': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'quai.meet': {
            'Meta': {'object_name': 'Meet'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Contact']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['quai']